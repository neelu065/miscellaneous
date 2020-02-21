% Plot a Bezier curve and a Bezier surface on a 3D graph with given control
% points

% B�zier curve of degree n is defined by a set of (n + 1) control
% points ki (n=2)
% Control points [x,y,z]
cp=cell(5,1);
cp{1,1}=[ 1.0, 0.0, 0.0];
cp{2,1}=[ 0.9, 0.0023, 0.0];
cp{3,1}=[ 0.6, 0.0020, 0.0];
cp{4,1}=[ 0.45, 0.006, 0.0];
cp{5,1}=[ -1.45, 0.0, 0.0];
cp{6,1}=[ 0.45, -0.006, 0.0];
cp{7,1}=[ 0.6, -0.002, 0.0];
cp{8,1}=[ 0.9, -0.0023, 0.0];
cp{9,1}=[ 1.0, 0.0, 0.0 ];
a = cp{1,1};
b = cp{2,1};
c = cp{3,1};
d = cp{4,1};
e = cp{5,1};
f = cp{6,1};
g = cp{7,1};
h = cp{8,1};
i = cp{9,1};
% Plotting vector (2001 points)
U=0:0.0005:1;
[Xout,Yout,Zout] = BezierCurve(cp,U);
% plot (2001 points)
%figure()
hold on
plot(Xout(:),Yout(:))
%plot(Xout(:),Yout(:),Zout(:))
hold on
plot(a(:,1),a(:,2))

plot(b(:,1),b(:,2))

plot(c(:,1),c(:,2))

plot(d(:,1),d(:,2))
plot(f(:,1),f(:,2))
plot(g(:,1),g(:,2))
plot(h(:,1),h(:,2))
plot(e(:,1),e(:,2))
plot(i(:,1),i(:,2))
% B�zier surface of degree (n, m) is defined by a set of (n + 1)(m + 1)
% control points ki,j
% Control points [x,y,z]
cp=cell(3,3);
cp{1,1}=[ 0.0, 0.0, 0.0];
cp{1,2}=[ 0.0, 1.0, 0.0];
cp{1,3}=[ 0.0, 2.0, 0.0];
cp{2,1}=[ 0.0, 0.0, 1.0];
cp{2,2}=[-1.0, 1.0, 1.0];
cp{2,3}=[ 0.0, 2.0, 1.0];
cp{3,1}=[ 0.0, 0.0, 2.0];
cp{3,2}=[ 0.0, 1.0, 2.0];
cp{3,3}=[ 0.0, 2.0, 2.0];
% Plotting vectors
U=0:0.05:1; % 1-direction (201 points)
V=0:0.05:1; % 2-direction (201 points)
[Xout,Yout,Zout] = BezierSurface(cp,U,V);
% plot (40401 points)
% figure()
% %scatter3(Xout(:),Yout(:),Zout(:))
% plot3(Xout(:),Yout(:),Zout(:),'b')
%
%__________________________________________________________________________
% Copyright (c) 2018
%     George Papazafeiropoulos
%     Captain, Infrastructure Engineer, Hellenic Air Force
%     Civil Engineer, M.Sc., Ph.D. candidate, NTUA
%     Email: gpapazafeiropoulos@yahoo.gr
% _________________________________________________________________________
