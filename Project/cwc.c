#include <stdio.h>
#include <string.h>

int main(){
    FILE *f = fopen("/home/phuoclong/cosel.c","w+");
    fputs("#include <stdio.h>\n",f);
    fputs("int main(){\n",f);
    fputs("\tint x, y;\n",f);
    fputs("\tchar c;\n",f);
    char s[] = "\"%d%c%d\"";
    char s2[] = "&x,&c,&y";
    fprintf(f,"\tscanf(%s,%s);\n",s,s2);
    for (int i = 1; i <= 500;i++)
        for (int j = 1; j <= 500;j++){
            fprintf(f,"\tif ((x == %d) && (c == %s) && (y == %d))\n",i,"'*'",j);
            fprintf(f,"\t\tprintf(%s,%d);\n","\"%d\"",i*j);
            
        }
    fputs("\n}",f);
    return 0;
}