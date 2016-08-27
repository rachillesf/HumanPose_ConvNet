debug = 0
for i = 1:10000
   
    10000 - i
    
    im_name = strcat('frame_images/frame',int2str(i-1),'.jpg');
    im = imread(im_name);
    loc = frame_locations{i};
    
    [n,m,~] = size(im);
    im = imresize(im,[220, 220],'bilinear');
    
    
    pos = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
           pos = [pos; [loc(j,1)*(220/n) loc(j,2)*(220/n) loc(j,3)]];
        end
    end
    
   
    savepath =   strcat('images220/frame',int2str(i-1),'.jpg');
    
    imwrite(im,savepath)
    locations{i} = pos;
    
    if debug ==1
        im_show = insertMarker(im,pos(:,1:2));
        imshow(im_show)
        button = waitforbuttonpress;
    
        if button == 1
            close all;
            break;
        end
    end
    

end

save('locations.mat','locations')