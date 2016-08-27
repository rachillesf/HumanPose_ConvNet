clear all;
load('joints.mat');
debug = 0;
for i = 1:10000
    10000 - i
    
    im_name = strcat('images/im',num2str(i,'%05i'),'.jpg');
    im = imread(im_name);
    loc = joints(:,:,i);
    
    [nl,nc,~] = size(im);
    v_loc = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
            v_loc = [v_loc; [loc(j,1) loc(j,2)]];
        end
    end
    
    xmin = min(v_loc(:,1)) ;
    xmin = xmin - 0.3*xmin;
    if xmin < 0
        xmin = 0;
    end
    
    xmax = max(v_loc(:,1));
    xmax = xmax + 0.3*xmax;
    if xmax > nc
        xmax = nc;
    end
    
    ymin = min(v_loc(:,2));
    ymin = ymin - 0.5*ymin;
    if ymin < 0
        ymin = 0;
    end
    
    ymax = max(v_loc(:,2));
    ymax = ymax + 0.3*ymax;
    if ymax > nl
        ymax = nl;
    end
    
    dx = xmax - xmin;
    dy = ymax - ymin;
    
    cla;
    crop = imcrop(im,[xmin,ymin,dx,dy]);
    
    new_x = v_loc(:,1) - xmin;
    new_y = v_loc(:,2) - ymin;
    
    new_loc = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
           new_loc = [new_loc; [loc(j,1)-xmin loc(j,2)-ymin 1]];
        
        else
           new_loc = [new_loc;[0 0 0]];
        end   
    end
    
    
    crop_locations{i} = new_loc;
    save_name = strcat('crop_images/im',num2str(i,'%05i'),'.jpg');
    imwrite(crop,save_name)
    
    
    if debug ==1
        
        im_show = insertMarker(crop,new_loc(:,1:2));
        imshow(im_show)
        button = waitforbuttonpress;
    
        if button == 1
            close all;
            break;
        end
    end
    
    
    
end
    
    