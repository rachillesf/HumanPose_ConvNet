clear all
load('joints.mat');
while 1
    %read random image and joints
    i = randi(10000);
    im_name = strcat('images/im',num2str(i,'%05i'),'.jpg');
    im = imread(im_name);
    loc = joints(:,:,i);
    
    [im,loc] = crop(im,loc);
    [im,loc] = frame(im,loc);
    [im,loc] = resize(im,loc);
    
    %take all visibles joints
    v_loc = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
            v_loc = [v_loc; [loc(j,1) loc(j,2)]];
        end
    end
     i
    loc
    
    im_show = insertMarker(im,v_loc);
    imshow(im_show)
    button = waitforbuttonpress;
   
    
    if button == 1
        close all;
        break;
    end
end