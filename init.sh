mkdir src
mkdir obj
mkdir bin
mkdir prgsrc
mkdir include

touch prgsrc/program.cpp
echo "int main(int argc, const char *argv[])" >> prgsrc/program.cpp
echo "{" >> prgsrc/program.cpp
echo "    " >> prgsrc/program.cpp
echo "    return 0;" >> prgsrc/program.cpp
echo "}" >> prgsrc/program.cpp
echo "" >> prgsrc/program.cpp

make clean

