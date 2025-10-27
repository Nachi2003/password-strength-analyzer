import argparse
import zxcvbn
import time

def analyze_password(password, user_info=[]):
    """
    Analyzes the strength of a given password using zxcvbn,
    checking against a list of user-provided words.
    """
    print(f"Analyzing password: '{'*' * len(password)}'")
    if user_info:
        # Show what personal words we are checking against
        print(f"Checking against: {user_info}")
    print("-" * 30)

    start_time = time.time()

    # --- THIS IS THE KEY CHANGE ---
    # We pass the user_info list to zxcvbn's user_inputs parameter
    results = zxcvbn.zxcvbn(password, user_inputs=user_info)

    end_time = time.time()
    analysis_time = (end_time - start_time) * 1000

    score = results.get('score')
    strength_map = {
        0: "❌ Very Weak (0/4)", 1: "🔥 Weak (1/4)",
        2: "⚠️ Fair (2/4)", 3: "✅ Good (3/4)", 4: "💪 Strong (4/4)"
    }
    print(f"Strength Score:   {strength_map.get(score, 'Unknown')}")

    crack_time = results.get('crack_times_display', {}).get('offline_slow_hashing_1e4_per_second', 'N/A')
    print(f"Est. Crack Time:  {crack_time} (offline, slow hash)")

    feedback = results.get('feedback', {})
    warning = feedback.get('warning')
    if warning:
        print(f"\nWarning:          {warning}")

    suggestions = feedback.get('suggestions', [])
    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"  - {suggestion}")

    sequence = results.get('sequence', [])
    if sequence:
        print("\nAnalysis of Password Components:")
        for part in sequence:
            token = part['token']
            pattern = part['pattern']

            # --- NEW FEATURE ---
            # Check if this part was one of the user's inputs
            if 'user_inputs' in part.get('dictionary_name', ''):
                print(f"  - Component: '...{token[-2:]}'")
                print(f"    - 🚨 Type: Personal Information ({pattern})")
                print(f"    - Matched: '{part.get('matched_word')}'")
            elif 'dictionary_name' in part:
                 print(f"  - Component: '...{token[-2:]}'")
                 print(f"    - Type: {pattern} ({part['dictionary_name']})")
            elif 'regex_name' in part:
                 print(f"  - Component: '...{token[-2:]}'")
                 print(f"    - Type: {pattern} (pattern: {part['regex_name']})")
            else:
                 print(f"  - Component: '...{token[-2:]}'")
                 print(f"    - Type: {pattern}")

    print(f"\nAnalysis completed in {analysis_time:.2f} ms")


def main():
    parser = argparse.ArgumentParser(
        description="A defensive tool to analyze password strength.",
        # Updated example to show the new -i flag
        epilog="Example: python strength_analyzer.py \"Fluffy1990\" -i Fluffy 1990"
    )

    parser.add_argument(
        "password",
        type=str,
        help="The password you want to analyze."
    )

    # --- NEW ARGUMENT ---
    # This adds the -i (or --inputs) flag
    parser.add_argument(
        "-i", "--inputs",
        nargs='+',  # This accepts one or more arguments
        default=[],
        help="A list of personal words to check against (e.g., name, pet, year)."
    )

    args = parser.parse_args()

    if args.password:
        # Pass the new list of inputs to our function
        analyze_password(args.password, args.inputs)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()