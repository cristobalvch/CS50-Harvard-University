#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
bool is_valid_key(string s);

int main(int argc, string argv[])
{
    if(argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (! is_valid_key(argv[1]))
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string s = get_string("plaintext: ");
    string difference = argv[1];
    for (int i = 'A'; i < 'Z'; i++)
        difference[ i - 'A'] = toupper(difference[ i - 'A']) -i;
    printf("ciphertext: ");
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isalpha(s[i]))
            s[i] = s[i] + difference[s[i] - (isupper(s[i]) ? 'A' : 'a')];
        printf("%c", s[i]);
    }
    printf("\n");
}

bool is_valid_key(string s)
{
    int len = strlen(s);
    if (len != 26)
        return false;

    int freq[26] = { 0 };
    for (int i = 0; i < len; i++)
    {
        if (!isalpha(s[i]))
            return false;
        int index = toupper(s[i]) - 'A';
        if (freq[index] >0)
            return false;
        freq[index]++;
    }
    return true;
}