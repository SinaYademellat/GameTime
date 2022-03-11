#include <bits\stdc++.h>
//Calculator : The Game (Hint)
using namespace std;
int MOVES=5;//MAXL
int GOAL=210;
int NUMBER_out=1;
int MAINFirstStap=0;
bool checkleaf(string t)
{
	int FirstStap=MAINFirstStap;
	for (int i=0;i<t.length();i+=2)
	{
		char C1=t[i];
		char C2=t[i+1];

		switch (C1)
		{
		case '`':
			FirstStap*=10;
			FirstStap+=(C2-'0');
			break;
		
		case '+':
			FirstStap+=(C2-'0');
			break;
		
		case '-':
			FirstStap-=(C2-'0');
			break;
				
		case '/':
			FirstStap/=(C2-'0');
			break;
		
		case '*':
			FirstStap*=(C2-'0');
			break;
		default:
			break;
		}	
	} 
	//cout<<FirstStap<<"\n";
	return FirstStap==GOAL;
}
int spaceSize=0;
string tmp_out_2="";
vector<string>foo;
void BT(int l)
{
	if(l==MOVES)
	{
		if(checkleaf(tmp_out_2))
		{
			cout<<"# "<<NUMBER_out++<<") "<<tmp_out_2<<endl;
		}
	}		
	else
	{
		for(int i=0;i<spaceSize;i++)
		{	
			//p
			tmp_out_2+=foo[i];
			BT(l+1);
			tmp_out_2.pop_back();
			tmp_out_2.pop_back();
		}
	}

}
int main()
{
	ios::sync_with_stdio(false); cin.tie(0);
	cout<<"cur_point: ";cin>>MAINFirstStap;
	cout<<"GOAL: ";cin>>GOAL;
	cout<<"MOVES: ";cin>>MOVES;
	int tadad=0;cout<<"NUMBER: ";cin>>tadad;	
	for (int i =1 ;i<=tadad;i++)
	{
		string tmpp="";
		cin>>tmpp;
		foo.push_back(tmpp);
	}
	spaceSize=tadad;
	BT(0);
}
