import media
import fresh_tomatoes

# 1.Your Name
your_name = media.Movie('Your Name',
                        'https://img1.doubanio.com/view/photo/l/public/p2395733377.webp',
                        'http://v.youku.com/v_show/id_XMTg0Mjk4Mzk5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')
# 2.Coco
coco = media.Movie('Coco',
                    'https://img1.doubanio.com/view/photo/l/public/p2503997609.webp',
                    'http://v.youku.com/v_show/id_XMzE4Nzc5MTE5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.1')
# 3.Thor: Ragnarok
thor = media.Movie('Thor: Ragnarok',
                    'https://img3.doubanio.com/view/photo/l/public/p2500451074.webp',
                    'http://v.youku.com/v_show/id_XMzEwNDY0Mjg2MA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.1')
# 4.X-Men: Apocalypse
x_man = media.Movie('X-Men: Apocalypse',
                    'https://img3.doubanio.com/view/photo/l/public/p2352321614.webp',
                    'http://v.youku.com/v_show/id_XMTU0ODQ0MzQ1Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')
# 5.Transformers: The Last Knight
transformers = media.Movie('Transformers: The Last Knight',
                    'https://img1.doubanio.com/view/photo/l/public/p2462475058.webp',
                    'http://v.youku.com/v_show/id_XMTg1MTc0ODg0OA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')
# 6.The Fate of the Furious
furious = media.Movie('The Fate of the Furious',
                    'https://img3.doubanio.com/view/photo/l/public/p2444256500.webp',
                    'http://v.youku.com/v_show/id_XMTg2MDY4OTQ2OA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1')

# define the list of my favourite movies
movies = [your_name, coco, thor, x_man, transformers, furious]
# construct a website through the func: open_movies_page
fresh_tomatoes.open_movies_page(movies)
