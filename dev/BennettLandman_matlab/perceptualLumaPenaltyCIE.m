function penalty = perceptualLumaPenaltyCIE(x,L,var)
B=reshape(x,[length(x(:))/3 3]);
% B = COLORSPACE('RGB->LAB',RGB);
Lstar = min(255,max(0,B(:,1)));
penalty=max((Lstar<L).*(exp((L-Lstar)/var)-1));
% penalty = 1e2*max(255*.65-min(Lstar),0)+5e1*max(1-exp(-((Lstar-L)/var).^2));
