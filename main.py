#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <vector>
#include <cctype>
#include <cmath>
#include <fstream>
using namespace std;
//problem 1
void file_writer(const string& text)
{
    ofstream out("output.txt");
    out << text;
    out.close();
}
string& file_reader(const string& filename)
{
    ifstream in(filename);
    string* str = new string((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
    return *str;
}
// problem 3
void add_excitement(string* arr, bool modify, int size)
{
    for(int i = 0; modify && i < size; ++i)
    {
        arr[i] += "!";
    }
}
// problem 4
int firstDiff(const char* a, const char* b)
{
    if (!(strcmp(a, b)))
    {
        return -1;
    }
    int i = 0, end = min(strlen(a), strlen(b));
    for(; (i < end) && a[i] == b[i]; ++i);
    return i;
}
//problem 5
int random_number(int n)
{
    int res = 0;
    for (int i = 0; i < n; ++i)
    {
        res *= 10;
        res += rand() % 10;
    }
    return res;
}
//problem 6
int closest(const int arr[], int n, int size)
{

    if ((*min(arr, arr + size)) > n)
    {
        std::cout << "Enter another array" << std::endl;
        return -1;
    }

    int d, minDiff, index;
    for(int i = 0; i < size; ++i)
    {
        d = n - arr[i];
        if (!i || (d >= 0 && d < minDiff))
        {
            minDiff = d;
            index = i;
        }
    }
    return arr[index];
}
//problem 7
int matches(const char* a, const char* b)
{
    int len = min(strlen(a), strlen(b)), matches = 0;
    for(int i = 0; i < len; ++i)
    {
        if (a[i] == b[i])
        {
            ++matches;
        }
    }
    return matches;
}
//problem 8
vector<int>& findall(const char* s, char c)
{
    vector<int>* locations = new vector<int>;
    int len = strlen(s);
    for(int i = 0; i < len; ++i)
    {
        if(s[i] == c)
        {
            locations->push_back(i);
        }
    }
    return *locations;
}
//problem 9
void change_case(string& s)
{
    int len = s.length();
    for(int i = 0; i < len; ++i)
    {
        if(isupper(s[i]))
        {
            s[i] = char(tolower(s[i]));
        }
        else if(islower(s[i]))
        {
            s[i] = char(toupper(s[i]));
        }
    }

}
//problem 10
bool is_sorted(const int arr[], int n)
{
    bool sorted = true;
    for(int i = 0; sorted && (i < n - 1); ++i)
    {
        sorted = arr[i] < arr[i + 1];
    }
    return sorted;
}
//problem 11
bool sum_even(int a, int b)
{
    return !((a + b) & 1);
}
//problem 14
void calc(const string& s)
{
    int letters = 0;
    int digits = 0;
    int len = s.length();
    for(int i = 0; i < len; ++i)
    {
        if(isalpha(s[i]))
        {
            ++letters;
        }
        else if(isdigit(s[i]))
        {
            ++digits;
        }
    }
    cout << letters << ' ' << digits << endl;
}
//problem 15
string& email_to_username(const string& email)
{
    string* s = new string(email.substr(0, email.find('@')));
    return *s;
}
//problem 16
void merge(int a[], int b[], int sizeA, int sizeB, int res[])
{
    std::merge (a,a + sizeA, b, b + sizeB, res);
}
//problem 17
double root(double x, int n = 2)
{
    return pow(x, double(1 / double(n)));
}

//problem 18
void wordFrequency()
{
    string str = file_reader("lab.txt");
    int strLen = str.length();
    string word = "";
    vector<string> words;
    map<string, int> freq;
    for(int i = 0; i < strLen; ++i)
    {
        if(isalpha(str[i]))
        {
            word += char(tolower(str[i]));
        }
        else if(word.length()){
            if (freq.find(word) == freq.end())
            {
                freq[word] = 1;
            }
            else
            {
                ++(freq[word]);
            }
            word.clear();
        }
    }
    for(map<string, int>::iterator it = freq.begin(); it != freq.end(); ++it)
    {
        cout << (*it).first << ' ' << (*it).second << endl;
    }
}
int main()
{
    srand(time(0));
    return 0;
}
