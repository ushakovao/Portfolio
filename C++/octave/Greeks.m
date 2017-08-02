m=6;
n=61;
S0=100;
S1=130;
K=115;
r=0.05;
T=1.0;
v=0.3;
time = transpose(linspace(T,0,m));
S=linspace(S0,S1,n);

function dj = d_j(j,S,K,r,v,T)
dj=(log(S/K) + (r + ((-1)^(j-1))*0.5*v*v)*(T-time))/(v*((T-time)^0.5));
endfunction




function d= norm_pdf(x) 
d= (1.0 ./((2 .*3.14) .^(0.5))).*exp(-0.5 .*x .*x);
endfunction

function d = norm_cdf(x)
k = 1.0 ./(1.0 + 0.2316419 .*x);
k_sum = k .*(0.319381530 + k .*(-0.356563782 + k.*(1.781477937 + k.*(-1.821255978 + 1.330274429 .* k))));
  if x >= 0.0
    d= (1.0 - (1.0 ./((2 .*3.14).^0.5)).*exp(-0.5 .*x.*x) .* k_sum);   
  else 
    d= 1.0 - norm_cdf(-x);
  end
endfunction



factor1 =bsxfun(@times,sigma*0.5*(1/sqrt((T-time)*2*pi), S)
factor2 = exp(-d1.^2/2)
factor3 = bsxfun(@times,r*K*exp(-r*(T-times)), normcdf(d2))
-factor1*factor2-factor3

%Call Price
function d=  call_price(S, K,r,v,T)
d= S .* norm_cdf(d_j(1, S, K, r, v, (T-time)))-K.*exp(-r*(T-time)) .* norm_cdf(d_j(2, S, K, r, v, (T-time)));
endfunction

%Calculate the European vanilla call Delta
function d =  call_delta(S, K, r, v,  T) 
d= norm_cdf(d_j(1, S, K, r, v, (T-time)));
endfunction



%Calculate the European vanilla call Gamma
function d = call_gamma(S,K,r,v,T) 
d= norm_pdf(d_j(1, S, K, r, v, (T-time)))./(S*v*sqrt((T-time)));
endfunction


%Calculate the European vanilla call Vega
function d =call_vega(S,K,r,v,T)
d = S.*norm_pdf(d_j(1, S, K, r, v, (T-time))).*sqrt((T-time));
endfunction

%Calculate the European vanilla call Theta
function d = call_theta(S,K,r,v, T)
d= -(S.*norm_pdf(d_j(1, S, K, r, v, (T-time))).*v)./(2.*sqrt((T-time)))- r.*K.*exp(-r.*(T-time)).*norm_cdf(d_j(2, S, K, r, v, (T-time)));
endfunction

%Calculate the European vanilla call Rho
function d = call_rho(S,K,r,v,T)
d = K.*(T-time).*exp(-r.*(T-time)).*norm_cdf(d_j(2, S, K, r, v, (T-time)));
endfunction

%Calculate the European vanilla put price 
function d = put_price(S,K,r,v,T)
d= -S.*norm_cdf(-d_j(1, S, K, r, v, (T-time)))+K.*exp(-r.*(T-time)) * norm_cdf(-d_j(2, S, K, r, v, (T-time)));
endfunction

%Calculate the European vanilla put Delta
function d = put_delta(S,K,r,v,T)
d= norm_cdf(d_j(1, S, K, r, v, (T-time))) - 1;
endfunction

%Calculate the European vanilla put Gamma
function d = put_gamma(S,K,r,v,T)
d= call_gamma(S, K, r, v, (T-time)); 
endfunction

%Calculate the European vanilla put Vega
function d= put_vega(S,K,r,v,T)
d= call_vega(S, K, r, v, (T-time)); 
endfunction

%Calculate the European vanilla put Theta
function d = put_theta(S,K,r,v,T)
d =-(S.*norm_pdf(d_j(1, S, K, r, v, (T-time))).*v)./(2 .*sqrt((T-time)))+ r.*K.*exp(-r.*(T-time)).*norm_cdf(-d_j(2, S, K, r, v, (T-time)));
endfunction

%Calculate the European vanilla put Rho
function d = put_rho(S,K,r,v,T)
d=-(T-time).*K.*exp(-r.*(T-time)).*norm_cdf(-d_j(2, S, K, r, v, (T-time)));
endfunction

Delta_c=put_delta(S, K, r, v,  T); 
Gamma_c = put_gamma(S,K,r,v,T);
Vega_c=put_vega(S,K,r,v,T);
Theta_c=put_theta(S,K,r,v,T);
Rho_c=put_rho(S,K,r,v,T);

subplot(1,5,1);
plot(S,Delta_c);
title("Delta")
xlabel('Option price');
ylabel('Delta');

subplot(1,5,2);
plot(S,Gamma_c);
title("Gamma")
xlabel('Asset price');
ylabel('Gamma');

subplot(1,5,3);
plot(S,Vega_c);
title("Vega");
xlabel('Asset price');
ylabel('Vega');

subplot(1,5,4);
plot(S,Theta_c);
title("Theta");
xlabel('Asset price');
ylabel('Theta');

subplot(1,5,5);
plot(S,Rho_c);
title("Rho");
xlabel('Asset price');
ylabel('Rho');  
