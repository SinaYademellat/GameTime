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

		//<<
		case '<':
			FirstStap/=10;
		default:
			break;
		}	
	} 
	//cout<<FirstStap<<"\n";
	return FirstStap==GOAL;
}
int spaceSize=0;

bool checkleaf_V(vector<string> t)
{
	int FirstStap=MAINFirstStap;
	for (int i=0;i<t.size();i++)
	{
		char C1=t[i][0]; // type
		string C2=t[i]; C2[0]='0'; // number :)
		int c2=stoi(C2);
		// cout<<"\nC2: "<<c2<<" "<<c2+1<<endl;
		int tmpNumber=1;
		for (int i = 1; i < C2.length(); i++)
		{
			tmpNumber*=10;
		}
		
		switch (C1)
		{
		case '`': // `a ==> cur[a] :)
			
			FirstStap*=tmpNumber;
			FirstStap+=c2;
			break;
		
		case '+':
			FirstStap+=c2;
			break;
		
		case '-':
			FirstStap-=c2;
			break;
				
		case '/':
			FirstStap/=c2;
			break;

		case '*':
			FirstStap*=c2;
			break;

		//<<
		case '<':
			FirstStap/=10;
		default:
			break;
		}	
	} 
	// cout<<FirstStap<<"\n";
	return FirstStap==GOAL;
}


vector<string>tmp_out_;
string tmp_out_2="";
vector<string>foo;
void BT(int l)
{
	if(l==MOVES)
	{
		if(checkleaf_V(tmp_out_))
		{
			cout<<"# "<<NUMBER_out++<<") ";
			for(string u: tmp_out_)
			{
				cout<<u<<" , ";
			}
			cout<<endl;
		}
	}		
	else
	{
		for(int i=0;i<spaceSize;i++)
		{	
			//p
			tmp_out_.push_back(foo[i]);
			BT(l+1);
			tmp_out_.pop_back();
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
	cout<<endl;
	BT(0);
}
