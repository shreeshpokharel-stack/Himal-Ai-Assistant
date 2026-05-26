from commands import execute_command

print("🤖 HimalAI Assistant")
print("=" * 50)

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    response = execute_command(command)

    print("HimalAI:", response)