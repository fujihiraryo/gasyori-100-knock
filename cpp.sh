g++ $1 -std=c++11 `pkg-config --cflags opencv` `pkg-config --libs opencv`
./a.out
rm ./a.out
