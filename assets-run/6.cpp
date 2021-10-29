#include <map>
#include<sstream>
#include<iostream>

using namespace std;

void wordsCount(string str){

      int count = 1;
      map<string,int> wordsMap;
      istringstream wordStream(str);

      string word;
       while(wordStream >> word){
             pair<map<string,int>::iterator,bool> retrunValue;

            retrunValue = wordsMap.insert( pair<string,int>(word,count));

            if (retrunValue.second==false)
            {
                  ++retrunValue.first->second; 
            }     
       }
       map<string,int>::iterator itr ;

       for (itr = wordsMap.begin(); itr != wordsMap.end(); ++itr){

               cout << itr->first ;
               cout<< '\t' << itr->second << '\n';
       }
}

int main(){
    string word;
    getline(cin,word);
      wordsCount(word);    

      return 0;

}