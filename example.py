# example.py

import procastinatrix as lib


def main():
    print("Instructions")
    print(lib.instructions())

    print("\nMotivation")
    print(lib.motivation())

    print("\nFake Productivity")
    activity = lib.fake_productivity()
    print("Suggested activity:", activity)

    print("\nSnack Recommendation")
    snack = lib.recommend_snack("stressed", 8)
    print("Recommended snack:", snack)

    print("\nBreak Suggestion")
    print(lib.break_excuse(150))

    print("\nProcrastination Plan")
    plan = lib.procrastination_plan("homework", urgency=7, guilt_level=5)
    print(plan)

    print("\nReward System")
    reward_msg = lib.reward("ice cream", "finishing your assignment")
    print(reward_msg)

    print("\nReturn to Work Message")
    message = lib.return_to_work_message("your project", 20)
    print(message)


if __name__ == "__main__":
    main()