%这个是人工的一个简单数据集
clear;
k=5;%knn的k
Ynew=[];%还原后的数据
I=ones(100,100);
I=I*5+randn(100,100);
Y=double(I);
Yg=mapminmax(Y);
a=fkNN(Yg,k);
[m,n]=size(Y);
W=zeros(n,n);
%******************************
%这一段的内容是查找是否在k近邻里面
 for i=1:n
     aa=a(i,1:k);
     aa(1)=0;
     for j=1:n
         if any(aa==j)
             W(i,j)=1;
             W(j,i)=1;
         end
     end
     W(i,i)=0;
 end
%****************************
%*********************************
%这一段是使用距离找确定最近邻
%for i=1:n
%    aa=a(i,k+1);
%     for j=1:n
%         if norm(Yg(:,i)-Yg(:,j))<=aa
%             W(i,j)=1;
%             W(j,i)=1;
%         end
%     end
% end
[Z, E] =   sparse_graph_LRR(Y,W, 0.1, 5, 8.0, 2.5, 0);
Ynew=Y*Z+E;