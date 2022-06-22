s = 1; e = 1; f1 = 0.6*0.6; f2 = 0.6*0.8;
mom = fill([1,1,0,0],[0,1,1,0],'b'); daspect([1,1,1]); hold on;
Tree = [mom]; axis([-4, 4, 0, 4.5]);
v = VideoWriter('PT.avi');
v.FrameRate = 2;
open(v);
for i = 1:10
    for j = s:e
        mom = Tree(j);
        x = mom.XData([2;3]); y = mom.YData([2,3]);
        dx = diff(x); dy = diff(y);
        px = x(1) + f1 * dx + f2 * dy; 
        py = y(1) + f1 * dy - f2 * dx;
        dau1 = square([x(1);y(1)], [px;py]);
        dau2 = square([px;py], [x(2);y(2)]);
        Tree = [Tree, dau1, dau2];
    end
    s = e+1;
    e = numel(Tree);
    frame = getframe(gcf);
    writeVideo(v,frame);
end
close(v);
function hndl = square(p1, p2)
    v1 = p2-p1;  v2 = [v1(2); -v1(1)];
    pts = [p1, p1+v2, p1+v1+v2, p2];
    hndl = fill(pts(1,:),pts(2,:),'b');
end
