clear all;
load('joints.mat')
new_joints = joints;
debug = 0;
for i = 1:10000
 10000-i

im_name = strcat('images/im',num2str(i,'%05i'),'.jpg');
im = imread(im_name);
loc = joints(:,:,i);
    
[im,loc] = crop(im,loc);
[im,loc] = frame(im,loc);
[im,loc] = resize(im,loc);

savename = strcat('images220/frame',num2str(i-1),'.jpg');
imwrite(im,savename)
new_joints(:,:,i) = loc;

if debug ==1
    loc
    im_show = insertMarker(im,loc(:,1:2));
    imshow(im_show)
    button = waitforbuttonpress;
    
    if button == 1
        close all;
        break;
    end
end


end

save('locations.mat','new_joints')