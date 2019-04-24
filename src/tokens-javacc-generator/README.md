# Tokens Java Compiler Compiler™ (JavaCC™) Generator

The token generator for JavaCC is an algorithm written in Python to give the information, get the tokens that we need for our lexical analyzer [.jj file].

## For its use

This project requires a CSV file with the name of the token as the first field and lexeme or regex as the second field. This CSV file can easily be generated in excel or google sheets, just like this:

![sample-file](imgs/sample-file.jpg)
![sample-file](imgs/sample-save.jpg)

After this you can run the script `python tokens-javacc-generator.py`:
```shell
# run command
python tokens-javacc-generator.py
```

You must provide the path of your .csv file, and then click enter.

The tokens should be generated in the console, copy-paste on your .jj file.

```
TOKEN:
{
        //TOKEN's name: t_conditional
        <t_conditional: "if"|"unless">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_elif
        <t_elif: "elif">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_parenthesis_group_open
        <t_parenthesis_group_open: "(">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_parenthesis_group_close
        <t_parenthesis_group_close: ")">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_colons
        <t_colons: ":">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_else
        <t_else: "else">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_bool
        <t_bool: "true"|"false">{  } : DEFAULT
}
TOKEN:
{
        //TOKEN's name: t_asiggnment
        <t_asiggnment: "=">{  } : DEFAULT
}
```

**For the moment, you should remove the double quotes for the outputs of regular expressions you provide in the .csv file. We will fix it in later versions.**