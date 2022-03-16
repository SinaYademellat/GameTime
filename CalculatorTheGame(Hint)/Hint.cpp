#include <bits\stdc++.h>
//Calculator : The Game (Hint)
using namespace std;
	//MAXL
int MOVES=5,GOAL=210,NUMBER_out=1, MAINFirstStap=0,spaceSize=0;
bool checkleaf(vector<string> t)
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


		if(C1 == '$')
		{
			string tmpL="",tmpR="",tmpFirst="";	
			bool Flag_ =true;
			for (int s = 1; s < t[i].length(); s++)
			{
				if( t[i][s] == '=')
				{
					s+=2;
					Flag_=false;
					//continue;
				}

				if(Flag_)
				{
					tmpL+=t[i][s];
				}
				else
				{
					tmpR+=t[i][s];
				}
				
				/* code */
			}
			
			tmpFirst=to_string(FirstStap);

			for (int  j = 0; j < tmpFirst.length(); j++)
			{
				if(tmpFirst[j]==tmpL[0])
				{
					tmpFirst[j]=tmpR[0];
				}
			}
			//cout<<"\nL: "<<tmpL<<" R:"<<tmpR<<endl;
			//cout<<"--> "<<tmpFirst<<"\n";
			FirstStap = stoi(tmpFirst);
			continue;
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
	//cout<<FirstStap<<"\n";
	return FirstStap==GOAL;
}
vector<string>tmp_out_,foo;

void ALL_(vector<string> a)
{
	cout<<endl;
	for (string U : a)
	{
		cout<<U<<" , ";
	}
	cout<<endl;
}

void BT(int l)
{
	if(l==MOVES)
	{
		//ALL_(tmp_out_);
		//return;

		if(checkleaf(tmp_out_))
		{
			cout<<"# "<<NUMBER_out++<<") ";
			for(string u: tmp_out_)
			{
				cout<<u<<" , ";
			}
			cout<<endl;
			return;
		}
	}		
	else
	{
		for(int i=0;i<spaceSize;i++)
		{	
			//p
			tmp_out_.push_back(foo[i]);
			//b
			BT(l+1);
			//p
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
