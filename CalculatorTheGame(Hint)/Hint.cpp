#include <bits\stdc++.h>
//Calculator : The Game (Hint)
using namespace std;
	//MAXL
int MOVES=5,GOAL=210,NUMBER_out=1, MAINFirstStap=0,spaceSize=0;

void ALL_(vector<string> a)
{
	cout<<endl;
	for (string U : a)
	{
		cout<<U<<" , ";
	}
	cout<<endl;
}


inline void PatternMatching(string &A,string B,string C)
{
    int lenC=C.length();
    int lenB=B.length();
    int pos = 0;
    int index;
    while((index = A.find(B, pos)) != string::npos) 
    {
        //cout<<index<<" "<<lenB<<endl;
        A.erase(index,lenB);
        //cout<<"E : "<<A<<endl;
        A.insert(index,C);
        //cout<<"I : "<<A<<endl;  
        pos+=(lenC-1);
    }
}

bool checkleaf(vector<string> t)
{
	// fast :)
	//if(t[0]=="/3" || t[0]=="/8"){return false;}
	
	long double FirstStap=MAINFirstStap;
	for (int i=0;i<t.size();i++)
	{
		char C1=t[i][0]; // type
		string C2=t[i]; C2[0]='0'; // number :)
		int c2 =0;
		// // for *-3 :: (level 49)
		if( C2.length()>=3 )
		{
			if( C2[1]=='+')
			{
				C2[1]='0';
				c2 =stoi(C2);
			}
			else if ( C2[1]=='-')
			{
				// cout<<"\t Hi \t";
				C2[1]='0';
				c2 =stoi(C2);
				c2=c2*(-1);
			}
			else
			{
				c2 =stoi(C2);
			}
			
		}
		else
		{
			c2 =stoi(C2);
		}
		
		
		// cout<<"\nC2: "<<c2<<" "<<c2+1<<" STR: "<<C2<<endl;
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

			// for (int  j = 0; j < tmpFirst.length(); j++){	if(tmpFirst[j]==tmpL[0]){	tmpFirst[j]=tmpR[0];}}

			// PatternMatching 
			PatternMatching(tmpFirst,tmpL,tmpR);

			//cout<<"\nL: "<<tmpL<<" R:"<<tmpR<<endl;
			//cout<<"--> "<<tmpFirst<<"\n";
			FirstStap = stoi(tmpFirst);
			continue;
		}

		switch (C1)
		{
		case '`': // `a ==> cur[a] :)
			
			FirstStap*=tmpNumber;
			if(FirstStap>=0)
			{
				FirstStap+=c2;
			}
			else
			{
				FirstStap-=c2;
			}
			
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
			break;
		//x^2
		case '^':
			FirstStap=pow(FirstStap,c2);
			break;
		
		//+/- ==> @0
		case '@':
			FirstStap*=(-1);
			break;

		default:
			break;
		}	
	} 
	// // DEBUG :)
	// ALL_(t);
	// cout<<FirstStap<<"\n";
	
	return FirstStap==GOAL;
}
vector<string>tmp_out_,foo;

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
