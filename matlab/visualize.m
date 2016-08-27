while 1
    %read random image and joints
    i = randi(10000);
    im_name = strcat('images220/frame',num2str(i-1),'.jpg');
    im = imread(im_name);
    loc = locations{i};
    
    %take all visibles joints
    v_loc = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
            v_loc = [v_loc; [loc(j,1) loc(j,2)]];
        end
    end
    
    im_show = insertMarker(im,v_loc);
    imshow(im_show)
    button = waitforbuttonpress;
    
    if button == 1
        close all;
        break;
    end
end