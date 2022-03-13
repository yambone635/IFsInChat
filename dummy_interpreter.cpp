/**
 * @author Eleanor Fris
 * @brief A simple program for testing input/output interactions for the Discord
 * InteractiveFictionBot. Will echo any arguments it's called with, and then
 * reverse and output any input it's given through stdio.
 * @version 0.1
 * @date 2022-03-12
 */

#include <iostream>
#include <cstring>

using namespace std;

#define MAX_INPUT_LENGTH 500

int main(int argc, char *argv[])
{
    // Echo any arguments given
    cout << "Called with arguments:" << endl;
    for (int i = 0; i < argc; i++) {
        cout << argv[i] << endl;
    }

    char inputString[MAX_INPUT_LENGTH] = "";
    char exitCommand[] = "exit";

    do {
        // Note: this will not put the terminating '\n' into inputString
        cin.getline(inputString, MAX_INPUT_LENGTH);

        char reversedString[MAX_INPUT_LENGTH];
        int inputIndex = strlen(inputString) - 1;
        int outputIndex = 0;

        if (inputIndex < 0) {
            cout << inputString;
            continue;
        }

        for (/* not needed */; inputIndex >= 0; outputIndex++, inputIndex--) {
            reversedString[outputIndex] = inputString[inputIndex];
        }
        // Terminate the string, since the above loop doesn't do that part
        // Note: "outputIndex" was already incremented to the right spot
        reversedString[outputIndex] = '\0';

        cout << reversedString << endl;
    } while (strcmp(inputString, exitCommand) != 0);

    return 0;
}
