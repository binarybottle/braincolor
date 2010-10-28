function diff = perceptualGroupwiseColorSimiliarityCIE(x,L)
% RGB=max(0,min(1,reshape(x,[length(x(:))/3 3])));
% B = COLORSPACE('RGB->LAB',RGB);
B=reshape(x,[length(x(:))/3 3]);
B(:,1) = min(255,max(0,B(:,1)));
B(:,2) = min(255,max(-255,B(:,2)));
B(:,3) = min(255,max(-255,B(:,3)));
N = size(B,1);
diff = 0;
offset = 0;
for l=1:length(L)
    D = zeros([L(l) L(l)]);
    for i=1:L(l)
        for j=1:L(l)
            if(j==i)
                D(i,j)=0;
            else
                D(i,j)=sum((B(i+offset,2:3)-B(j+offset,2:3)).^2);
            end
        end
    end
    diff = diff + sum(max(D));  
    offset = offset+L(l);
end
