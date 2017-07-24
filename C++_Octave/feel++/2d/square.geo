h=0.2;
Point(1) = {0,0,0,h};
Point(2) = {0,0.5, h/2};
Point(3) = {0,1,0,h};
Point(4) = {1,1,0,h};
Point(5) = {1,0,0,h};
Point(6) = {0.5,0,0,h/2 };
Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,5};
Line(5) = {5,6};
Line(6) = {6,1};
Line Loop(6) = { 1, 2, 3, 4,5,6};
Plane Surface(6) = {6};
Physical Line("in") = {1, 2, 6, 5};
Physical Line("out") = {3,4};
Physical Surface("Omega") = {6};
                                
