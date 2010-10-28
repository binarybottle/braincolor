function err = perceptualPairwiseDiffCIE(x)
B=reshape(x,[length(x(:))/3 3]);
B(:,1) = min(255,max(0,B(:,1)));
B(:,2) = min(255,max(-255,B(:,2)));
B(:,3) = min(255,max(-255,B(:,3)));
% B = COLORSPACE('RGB->LAB',RGB);
N = size(B,1);
D = zeros([N N]);
for i=1:N
    for j=1:N
        if(j==i)
            D(i,j)=inf;
        else
        D(i,j)=sum((B(i,:)-B(j,:)).^2);
        end
    end
end
err = sum(min(D));