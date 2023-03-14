import sys,click
from  gc_scraper import get_search_data
from gmail import gmail_login
from ecalender import mark_event
from todo import todo
@click.group()
@click.version_option("1.0.1")
def main():
    """welcome to CLI-pal"""
    print("hi")
    pass
@main.command()
@click.argument("query",required=True)
def google_search(**kwargs):
    """google a keyword"""
    results = get_search_data(kwargs.get("query"))
    click.echo(results)
    pass
@main.command()
@click.argument('id', nargs=-1)
@click.argument('pas', nargs=1)
def gmail(**kwargs):
    """login to gmail"""
    id=kwargs.get("id")
    pas=kwargs.get("pas")
    results = gmail_login(id,pas)
    click.echo(results)
    pass

@main.command()
@click.argument('file_path', nargs=1)
def calendar(**kwargs):
    """mark events in calendar"""
    file_path=kwargs.get("file_path")
    mark_event(file_path)
    pass

@main.command
@click.argument("task", required=True)
def add_todo(**kwargs):
    '''add task'''
    task=kwargs.get("task")
    todo(task)
    pass



if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("SCRAPE")
    main()