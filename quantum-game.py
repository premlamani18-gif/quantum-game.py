import random

def quantum_ball_game():
    print("\nQuantum Ball game")
    print("System contains: Red, Red, Green")                                            
    print("Before measurement -> all possibilities exist (superposition)")

    # Quantum-like system (2 Red, 1 Green)
    balls = ["Red", "Red", "Green"]

    input("\nPress Enter to MEASURE (pick a ball)...")

    print("Measuring... collapsing state!\n")

    # Random selection (probability)
    result = random.choice(balls)

    guess = input("Guess the result (Red/Green): ").strip().lower()

    if guess == "red" and "Red" in result:
        print(f"Correct! It was {result}")
    elif guess == "green" and "Green" in result:
        print(f"Correct! It was {result}")
    else:
        print(f"Wrong! It was {result}")

    print("\nConcept:")
    print("- Red has higher probability (2/3)")
    print("- Green has lower probability (1/3)")
    print("- Measurement selects one outcome\n")


def main():
    while True:
        quantum_ball_game()

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Quantum world is fun")
            break


if __name__ == "__main__":
    main()

    # Quantum-like system (2 Red, 1 Green)
    

    
