import os

# Specify the directory containing the files
directory = 'img/eng_pics'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Generate HTML block for each file
    html = f'''
<div class="col-md-2">
    <a class="fancybox" rel="group" href="img/eng_pics/{filename}">
        <div class="img-wrap">
            <div class="overlay">
                <i class="fa fa-search"></i>
            </div>
            <img src="img/eng_pics/{filename}" alt=""/>
        </div>
    </a>
</div>
    '''
    # Print or save the HTML block
    print(html)