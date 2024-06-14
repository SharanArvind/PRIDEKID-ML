import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Function to generate content based on user input
def generate_content(user_input):
    sections = ["Definition:", "Awareness:", "Real-time Example:", "Context (points to consider):"]
    section_texts = []
    
    if user_input == 1:
        prompt = "Safety measures to avoid unnecessary problems:\n"
    elif user_input == 2:
        prompt = "Tracking moving objects which require sustained visual focus demands:\n"
    elif user_input == 3:
        prompt = "Identifying specific information that involves sensory classification:\n"
    elif user_input == 4:
        user_input = input("Enter your custom prompt: ")
        prompt = f"{user_input}:\n"
    else:
        return "Invalid input. Please choose a number from 1 to 4."

    for section in sections:
        prompt += section + "\n"
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=prompt,
            max_tokens=100,  # Adjust max tokens as needed
            temperature=0.7,  # Adjust temperature as needed
            top_p=1.0,
            n=1
        )
        section_text = response.choices[0].text.strip()
        prompt += section_text + "\n"
        section_texts.append(section_text)

    return "\n".join(section_texts)

# Main function to handle user interaction
def main():
    while True:
        print("\nChoose an option:")
        print("1. Safety measures to avoid unnecessary problems")
        print("2. Tracking moving objects which require sustained visual focus demands")
        print("3. Identifying specific information that involves sensory classification")
        print("4. Enter a custom prompt")
        print("5. Exit")

        option = input("Enter your choice (1-4): ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                output = generate_content(option)
                print("\nGenerated Content:\n" + output)
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
