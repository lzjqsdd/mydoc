# 自定义电子书阅读器选项

### Begin group: DEFAULT
 
# remember window size
# 保存上次使用窗口大小
remember_window_size = False
 
# user css
# 设定用户 CSS 样式表。它将可以自定义所有书籍的外观。
user_css = u'@import url(http://fonts.googleapis.com/css?family=Inconsolata);\n@import url(http://fonts.googleapis.com/css?family=PT+Sans);\n@import url(http://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700);\narticle,\naside,\ndetails,\nfigcaption,\nfigure,\nfooter,\nheader,\nhgroup,\nnav,\nsection,\nsummary {\n  display: block;\n}\naudio,\ncanvas,\nvideo {\n  display: inline-block;\n}\naudio:not([controls]) {\n  display: none;\n  height: 0;\n}\n[hidden] {\n  display: none;\n}\nhtml {\n  font-family: sans-serif;\n  -webkit-text-size-adjust: 100%;\n  -ms-text-size-adjust: 100%;\n}\nbody {\n  margin: 0;\n}\na:focus {\n  outline: thin dotted;\n}\na:active,\na:hover {\n  outline: 0;\n}\nh1 {\n  font-size: 2em;\n}\nabbr[title] {\n  border-bottom: 1px dotted;\n}\nb,\nstrong {\n  font-weight: bold;\n}\ndfn {\n  font-style: italic;\n}\nmark {\n  background: #ff0;\n  color: #000;\n}\ncode,\nkbd,\npre,\nsamp {\n  font-family: monospace, serif;\n  font-size: 1em;\n}\npre {\n  white-space: pre-wrap;\n  word-wrap: break-word;\n}\nq {\n  quotes: "\\201C" "\\201D" "\\2018" "\\2019";\n}\nsmall {\n  font-size: 80%;\n}\nsub,\nsup {\n  font-size: 75%;\n  line-height: 0;\n  position: relative;\n  vertical-align: baseline;\n}\nsup {\n  top: -0.5em;\n}\nsub {\n  bottom: -0.25em;\n}\nimg {\n  border: 0;\n}\nsvg:not(:root) {\n  overflow: hidden;\n}\nfigure {\n  margin: 0;\n}\nfieldset {\n  border: 1px solid #c0c0c0;\n  margin: 0 2px;\n  padding: 0.35em 0.625em 0.75em;\n}\nlegend {\n  border: 0;\n  padding: 0;\n}\nbutton,\ninput,\nselect,\ntextarea {\n  font-family: inherit;\n  font-size: 100%;\n  margin: 0;\n}\nbutton,\ninput {\n  line-height: normal;\n}\nbutton,\nhtml input[type="button"],\ninput[type="reset"],\ninput[type="submit"] {\n  -webkit-appearance: button;\n  cursor: pointer;\n}\nbutton[disabled],\ninput[disabled] {\n  cursor: default;\n}\ninput[type="checkbox"],\ninput[type="radio"] {\n  box-sizing: border-box;\n  padding: 0;\n}\ninput[type="search"] {\n  -webkit-appearance: textfield;\n  -moz-box-sizing: content-box;\n  -webkit-box-sizing: content-box;\n  box-sizing: content-box;\n}\ninput[type="search"]::-webkit-search-cancel-button,\ninput[type="search"]::-webkit-search-decoration {\n  -webkit-appearance: none;\n}\nbutton::-moz-focus-inner,\ninput::-moz-focus-inner {\n  border: 0;\n  padding: 0;\n}\ntextarea {\n  overflow: auto;\n  vertical-align: top;\n}\ntable {\n  border-collapse: collapse;\n  border-spacing: 0;\n}\nhtml {\n  font-family: \'PT Sans\', sans-serif;\n}\npre,\ncode {\n  font-family: \'Inconsolata\', sans-serif;\n}\nh1,\nh2,\nh3,\nh4,\nh5,\nh6 {\n  font-family: \'PT Sans Narrow\', sans-serif;\n  font-weight: 700;\n}\nhtml {\n  background-color: #eee8d5;\n  color: #657b83;\n  margin: 1em;\n}\nbody {\n  background-color: #fdf6e3;\n  margin: 0 auto;\n  max-width: 23cm;\n  border: 1pt solid #93a1a1;\n  padding: 1em;\n}\ncode {\n  background-color: #eee8d5;\n  padding: 2px;\n}\na {\n  color: #b58900;\n}\na:visited {\n  color: #cb4b16;\n}\na:hover {\n  color: #cb4b16;\n}\nh1 {\n  color: #d33682;\n}\nh2,\nh3,\nh4,\nh5,\nh6 {\n  color: #859900;\n}\npre {\n  background-color: #fdf6e3;\n  color: #657b83;\n  border: 1pt solid #93a1a1;\n  padding: 1em;\n  box-shadow: 5pt 5pt 8pt #eee8d5;\n}\npre code {\n  background-color: #fdf6e3;\n}\nh1 {\n  font-size: 2.8em;\n}\nh2 {\n  font-size: 2.4em;\n}\nh3 {\n  font-size: 1.8em;\n}\nh4 {\n  font-size: 1.4em;\n}\nh5 {\n  font-size: 1.3em;\n}\nh6 {\n  font-size: 1.15em;\n}\n.tag {\n  background-color: #eee8d5;\n  color: #d33682;\n  padding: 0 0.2em;\n}\n.todo,\n.next,\n.done {\n  color: #fdf6e3;\n  background-color: #dc322f;\n  padding: 0 0.2em;\n}\n.tag {\n  -webkit-border-radius: 0.35em;\n  -moz-border-radius: 0.35em;\n  border-radius: 0.35em;\n}\n.TODO {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #2aa198;\n}\n.NEXT {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #268bd2;\n}\n.ACTIVE {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #268bd2;\n}\n.DONE {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #859900;\n}\n.WAITING {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #cb4b16;\n}\n.HOLD {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #d33682;\n}\n.NOTE {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #d33682;\n}\n.CANCELLED {\n  -webkit-border-radius: 0.2em;\n  -moz-border-radius: 0.2em;\n  border-radius: 0.2em;\n  background-color: #859900;\n}\n'
 
# max fs width
# 设置在全屏显示模式下书籍的文字和图片的最大宽度。这会使您以适当的宽度来阅读图书。
max_fs_width = 800
 
# max fs height
# Set the maximum height that the book's text and pictures will take when in fullscreen mode. This allows you to read the book text without it becoming too tall. Note that this setting only takes effect in paged mode (which is the default mode).
max_fs_height = -1
 
# fit images
# 重新调整阅读器中的图像大小，使其以合适的尺寸显示。
fit_images = True
 
# hyphenate
# 断词分行文本
hyphenate = False
 
# hyphenate default lang
# 默认使用断词分行规则的语言
hyphenate_default_lang = u'en_us'
 
# search online url
# The URL to use when searching for selected text online
search_online_url = u'https://www.google.com/search?q={text}'
 
# remember current page
# 退出时保存当前文档的阅读位置
remember_current_page = True
 
# copy bookmarks to file
# Copy bookmarks to the ebook file for easy sharing, if possible
copy_bookmarks_to_file = True
 
# wheel flips pages
# 可用滚轮翻页
wheel_flips_pages = False
 
# wheel scroll fraction
# Control how much the mouse wheel scrolls by in flow mode
wheel_scroll_fraction = 100
 
# line scroll fraction
# Control how much the arrow keys scroll by in flow mode
line_scroll_fraction = 100
 
# tap flips pages
# Tapping on the screen turns pages
tap_flips_pages = True
 
# line scrolling stops on pagebreaks
# 防止向上和向下箭头键控制前一页滚动
line_scrolling_stops_on_pagebreaks = False
 
# page flip duration
# 翻页动画秒数，默认半秒。
page_flip_duration = 0.5
 
# font magnification step
# 点击增大/减少字体按钮时字体变化的幅度。值应该为 0 和 1 之间的一个数字。
font_magnification_step = 0.2
 
# fullscreen clock
# 全屏显示模式下显示时钟。
fullscreen_clock = False
 
# fullscreen pos
# 全屏显示模式下显示当前阅读位置。
fullscreen_pos = False
 
# fullscreen scrollbar
# 全屏显示模式下显示滚动栏。
fullscreen_scrollbar = True
 
# start in fullscreen
# 以全屏显示模式启动阅读器
start_in_fullscreen = True
 
# show fullscreen help
# 显示全屏用法帮助
show_fullscreen_help = True
 
# cols per screen
cols_per_screen = 1
 
# cols per screen portrait
cols_per_screen_portrait = 1
 
# cols per screen landscape
cols_per_screen_landscape = 1
 
# cols per screen migrated
cols_per_screen_migrated = True
 
# use book margins
use_book_margins = False
 
# top margin
top_margin = 20
 
# side margin
side_margin = 40
 
# bottom margin
bottom_margin = 20
 
# text color
text_color = None
 
# background color
background_color = None
 
# show controls
show_controls = True
 

### Begin group: FONTS
# 字体选项
 
# serif family
# 衬线字体
serif_family = u'Liberation Serif'
 
# sans family
# 非衬线字体
sans_family = u'Liberation Sans'
 
# mono family
# 等宽字体
mono_family = u'\u6587\u6cc9\u9a7f\u7b49\u5bbd\u5fae\u7c73\u9ed1'
 
# default font size
# 标准字体大小 px 值
default_font_size = 20
 
# mono font size
# 等宽字体大小 px 值
mono_font_size = 16
 
# standard font
# 标准字体类型
standard_font = u'serif'
 
# minimum font size
# 最小字体大小(px)
minimum_font_size = 8
 


