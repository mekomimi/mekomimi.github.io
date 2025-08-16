cd C:\Users\MI\Desktop\mekomimi.github.io\img

::mogrify -resize 400x *.webp

::mogrify -resize 400x600! -quality 85% -path ./resized *.webp

mkdir resized
for img in *.webp; 
    do convert "$img" -resize 400x600 "resized/$img"; 
done


pause