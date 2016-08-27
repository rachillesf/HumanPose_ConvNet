%script que adiciona um frame na imagem para deixa-la quadrada
%e corrige isso nas coordenadas
clear all
load('crop_locations.mat')
debug = 0
for i = 1:10000
    10000-i
    im_name = strcat('crop_images/im',num2str(i,'%05i'),'.jpg');
    im = imread(im_name);
    loc = crop_locations{i};
    
    new_loc = loc
    
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
    

    
    savepath =   strcat('frame_images/frame',int2str(i-1),'.jpg');
    imwrite(im,savepath)
    frame_locations{i} = new_loc;
    
    if debug ==1
        im_show = insertMarker(im,new_loc(:,1:2));
        imshow(im_show)
        button = waitforbuttonpress;
    
        if button == 1
            close all;
            break;
        end
    end
end

  save('frame_locations.mat','frame_locations')
        
        
    
    
 
