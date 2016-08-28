function [new_im,new_loc] = frame(im,loc)

    new_loc = loc;
    
    [h,w,n] = size(im);
    
    if w>h
        frame = ones( round((w-h)/2) ,w ,3 )*mean(mean(mean(im)));
        im = cat(1, frame, im,frame);
         for j = 1:length(new_loc)
             new_loc(j,:) = new_loc(j,:) + [0,round((w-h)/2),0];
         end 
    end    
    
    if h>w
         frame = ones(  h,round((h-w)/2) ,3 )*mean(mean(mean(im)));
         im = cat(2, frame, im,frame);
         for j = 1:length(new_loc)
             new_loc(j,:) = new_loc(j,:) + [round((h-w)/2),0,0];
         end 
         
    end

    new_im = im;

end