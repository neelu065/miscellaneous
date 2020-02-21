clear all
close all
clc
P00=[0  0 0];
P01=[-5 0 18];
P02=[-7 0 32];
P03=[0  0 50];
P10=[0  1 0];
P11=[-5 1 18];
P12=[-7 1 32];
P13=[0  1 50];
P20=[0  2 0];
P21=[-5 2 18];
P22=[-7 2 32];
P23=[0  2 50];
P30=[0  3 0];
P31=[-5 3 18];
P32=[-7 3 32];
P33=[0  3 50];

p0=[P00;P01;P02;P03];
p1=[P10;P11;P12;P13];
p2=[P20;P21;P22;P23];
p3=[P30;P31;P32;P33];
%write 4 curves
r0=bezret(p0);
r1=bezret(p1);
r2=bezret(p2);
r3=bezret(p3);
B=[];
n=length(r0);
for i=1:n
    B(1:4,(3*i-2):3*i)=[r0(i,:);r1(i,:);r2(i,:);r3(i,:)];
    bez3d(B(1:4,(3*i-2):3*i))
end


%{
R=bez3d(p);
R=bez3d(p);
R=bez3d(p);
%arrange lementwise
%run bezier on all and plot
%}