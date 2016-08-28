function [new_im,new_loc] = resize(im,loc)
    [n,m,~] = size(im);
    im = imresize(im,[220, 220],'bilinear');
    
    
    pos = [];
    for j = 1:length(loc)
        if loc(j,3) == 1
           pos = [pos; [loc(j,1)*(220/n) loc(j,2)*(220/n) loc(j,3)]];
        else 
           pos = [pos; [loc(j,1)*(220/n) loc(j,2)*(220/n) 0]];
        end
    end
    
   
   new_loc = pos;
   new_im = im;
    
    
end
    
 