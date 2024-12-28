import typer
import os

available_tech = [
    "r",
    "symfony",
    "textpattern",
    "elixir",
    "scrivener",
    "leiningen",
    "java",
    "plone",
    "delphi",
    "lithium",
    "drupal",
    "actionscript",
    "android",
    "lua",
    "gcov",
    "appceleratortitanium",
    "fortran",
    "cakephp",
    "cmake",
    "haskell",
    "rails",
    "mercury",
    "episerver",
    "license",
    "twincat3",
    "objective-c",
    "d",
    "yeoman",
    "gradle",
    "perl",
    "joomla",
    "racket",
    "waf",
    "agda",
    "kotlin",
    "playframework",
    "coq",
    "packer",
    "maven",
    "scala",
    "grails",
    "forcedotcom",
    "elisp",
    "tex",
    "gwt",
    "zig",
    "typo3",
    "readme",
    "expressionengine",
    "jboss",
    "sass",
    "zendframework",
    "unrealengine",
    "extjs",
    "kicad",
    "swift",
    "community",
    "prestashop",
    "sketchup",
    "ruby",
    "dart",
    "ros",
    "elm",
    "smalltalk",
    "opa",
    "archlinuxpackages",
    "global",
    "turbogears2",
    "nanoc",
    "ballerina",
    "modelica",
    "flaxengine",
    "oracleforms",
    "metaprogrammingsystem",
    "appengine",
    "qooxdoo",
    "ecu-test",
    "contributing",
    "vvvv",
    "ocaml",
    "visualstudio",
    "node",
    "nim",
    "codeigniter",
    "go",
    "sugarcrm",
    "jenkins_home",
    "labview",
    "lemonstand",
    "chefcookbook",
    "rhodesrhomobile",
    "stella",
    "scheme",
    "raku",
    "rescript",
    "opencart",
    "processing",
    "erlang",
    "finale",
    "c++",
    "eagle",
    "godot",
    "igorpro",
    "concrete5",
    "githubpages",
    "craftcms",
    "fuelphp",
    "cuda",
    "jekyll",
    "lilypond",
    "firebase",
    "dm",
    "seamgen",
    "clojure",
    "composer",
    "commonlisp",
    "magento",
    "sdcc",
    "rust",
    "purescript",
    "wordpress",
    "al",
    "terraform",
    "qt",
    "xojo",
    "symphonycms",
    "idris",
    "zephir",
    "ada",
    "unity",
    "julia",
    "kohana",
    "fancy",
    "cfwheels",
    "scons",
    "c",
    "phalcon",
    "iar",
    "laravel",
    "yii",
    "python",
    "autotools",
    "gitbook",
    'django',
    'nest',
    'nextjs',
    'reactnative'
]

app = typer.Typer()


@app.command()
def solo(name: str):

    current_dir = os.getcwd()

    tech = name.lower()

    variable_path = f"{current_dir}/gitignore/{tech}.gitignore"

    file = open(".gitignore", "a+")

    file_specific = open(variable_path, "r")

    if tech in available_tech:
        content = file_specific.readlines()
        file.write(f"#-->{tech}\n")
        file.writelines(content)
        file.write("\n")
        file.close()
        file_specific.close()

    typer.echo("Wallah! it's done!")


@app.command()
def many(count: int):

    current_dir = os.getcwd()

    list_of_each_tech = []

    for i in range(count):
        each_tech = typer.prompt(
            "Enter the languages, framework or libraries one by one"
        )
        list_of_each_tech.append(each_tech)

    for times in range(count):
        name = list_of_each_tech[times]

        tech = name.lower()

        file = open(".gitignore", "a+")

        variable_path = f"{current_dir}/gitignore/{tech}.gitignore"

        file_specific = open(variable_path, "r")

        if tech in available_tech:
            content = file_specific.readlines()
            file.write(f"#-->{tech}\n")
            file.writelines(content)
            file.write("\n")
            file.close()
            file_specific.close()

        typer.echo("Wallah! it's done!")


if __name__ == "__main__":
    app()
