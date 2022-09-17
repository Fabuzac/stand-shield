header = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Firefox history</title>
                <style>
                body {
                    background-color: #f1f1f1;
                    margin-left: 30%;
                }
                table, tbody, tr, td {
                    border: 2px solid rgb(0, 0, 0);
                    border-radius: 1em;
                    padding: 7px;
                }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <th>URL</th>
                        <th>DATE</th>
                    </tr>
        """
footer = """
        </table>
    </body>
    </html>
"""