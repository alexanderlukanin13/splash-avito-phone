import argparse
import sys
import requests


LUA_AVITO_PHONE = """
function main(splash)
    splash:go(splash.args.url)
    splash:wait(10)
    splash:runjs([[
    
        var targetNode = document.querySelector("button.item-phone-button");
        targetNode.textContent = 'FOUND';
        if (targetNode) {
            //--- Simulate a natural mouse-click sequence.
            triggerMouseEvent (targetNode, "mouseover");
            triggerMouseEvent (targetNode, "mousedown");
            triggerMouseEvent (targetNode, "mouseup");
            triggerMouseEvent (targetNode, "click");
        }
        else
            console.log ("*** Target node not found!");
        
        function triggerMouseEvent (node, eventType) {
            var clickEvent = document.createEvent ('MouseEvents');
            clickEvent.initEvent (eventType, true, true);
            node.dispatchEvent (clickEvent);
        }
    
    ]])
    splash:wait(10)
    return splash:png()
end
"""


def __parse_args(argv):
    parser = argparse.ArgumentParser(description='Get phone number from avito.ru via Splash')
    parser.add_argument('url')
    parser.add_argument('-o', '--output-png', default='output.png')
    return parser.parse_args(argv)


def main(argv):
    args = __parse_args(argv)
    response = requests.post('http://localhost:8050/execute', json={
        'url': args.url,
        'lua_source': LUA_AVITO_PHONE,
        'timeout': 30
    })
    with open(args.output_png, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main(sys.argv[1:])
