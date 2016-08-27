clear all
debug = 0;

for i = 1:1000
   
    1000 - i
    
    im_name = strcat('test_images/frame',int2str((11000+i)-1),'.jpg');
    im = imread(im_name);
  
   
    savepath =   strcat('test_images1/frame',int2str((i)-1),'.jpg');
    
    imwrite(im,savepath)
    
    
end

