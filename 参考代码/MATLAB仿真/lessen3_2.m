clear all;
close all;
RF1=2.3*1e7;%230MHz
RF2=3.3*1e7;%330MHz
RF3=2.5*1e7;%250MHz
PW=8*1e-5;%80us
PRI=4*1e-4;%400us
PA=1;
per=PW/PRI;
N=PRI*RF2;
t=linspace(0,5*PRI,20*N);
y1=(1+square(2*pi*t/PRI,100*per))/2;
y2=(1+square(2*pi*(t-1e-5)/PRI,100*per))/2;
y3=(1+square(2*pi*(t-2*1e-5)/PRI,100*per))/2;
x1=(1+sin(1000*pi*RF1*t))/2;
x2=(1+sin(1000*pi*RF2*t))/2;
x3=(1+sin(1000*pi*RF3*t))/2;
z1=y1.*x1;
z2=y1.*x2;
z3=y1.*x3;
z4=y2.*x1;
z5=y2.*x2;
z6=y2.*x3;
z7=y3.*x1;
z8=y3.*x2;
z9=y3.*x3;
y=(z1+z2+z3)/3;
yd=(z4+z5+z6)/3;
yd2=(z7+z8+z9)/3;
subplot(311);
plot(t,y);
title('频率分集同时发射');
subplot(312);
plot(t,yd);
title('频率分集延时10us发射');
subplot(313);
plot(t,yd2);
title('频率分集延时20us发射');