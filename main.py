# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:52:17 2022

@author: MAD_MAL1CE
"""

import praw
import random
import time
import openai
import math
import re

print(praw.__path__)
openai.api_key = 'OpenAI Key Here'

#The time in seconds between posts
cooldown = 5
bot_name = "clone_trooper_bot"
 
# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "clone_bot_id"

# Connecting your bot to your personal script app and logging in
reddit = praw.Reddit('CloneTrooper')
print("Logged In Successfully!")

def Get_Triggers():
    
    clone_triggers = ['clone', 'trooper', 'hevy', '501st']
    follow_orders_triggers = ["follow orders"]
    prisoners_triggers = ["do we take prisoners"]
    the_creeps_triggers = ['the creeps','creeped out', 'give me the creeps', 'creep me out', 'creeps me out']
    skirata_triggers = ["skirata"]
    sentient_triggers = ['sentient', 's e n t i e n t', 'sentience']
    order_66_triggers = ['order 66', 'order sixty six', 'order sixty-six']
    order_67_triggers = ["order 67"]
    order_69_triggers = ['order 69', 'order sixty nine', 'order sixty-nine']
    expendable_triggers = ['die', 'dying', 'dead', 'expendable']
    
    bark_triggers_txt = open('triggers/bark_triggers.txt', 'r')
    bark_triggers = bark_triggers_txt.read().splitlines()
    bark_triggers_txt.close()
    
    lightsaber_triggers = ["lightsaber", "light saber", "lasersword", "laser sword"]
    why_triggers = ["why", "explain", "i dont understand"]
    war_triggers = [" war", "war ", "wars ", " wars"]
    programmed_triggers = ["programmed", "programming", "thinking", "intelligent", "smart"]
    redredgreen_triggers = ["red red green", "red green red"]
    egg_triggers = [" egg", "egg ", " eggs", "eggs "]
    
    return clone_triggers, follow_orders_triggers, prisoners_triggers, the_creeps_triggers, expendable_triggers, lightsaber_triggers, why_triggers, war_triggers, programmed_triggers, redredgreen_triggers, egg_triggers, skirata_triggers, sentient_triggers, order_66_triggers, order_67_triggers, order_69_triggers, bark_triggers

def Get_Permission():
    
    #Make sure to add "import math" and "import re" at the top of your code.
    print("Getting Permission to Reply...")
    permission = True
    other_triggers = False
    
    if any(word in comment_lower for word in all_other_triggers):
        print("Other Bots Triggered!")
        other_triggers = True
        bot_list = [str(bot_name)] #Make sure you include bot_name = "Your Bot Name" in your variables
        
        #Comment out your own bot in this section
        if any(word in comment_lower for word in ahsoka_triggers):
            bot_list.append("Ahsoka_Tano_Bot")
        if any(word in comment_lower for word in anakin_triggers):
            bot_list.append("Anakin_Skywalker_Bot")
        if any(word in comment_lower for word in rex_triggers):
            bot_list.append("Captain_Rex_Bot")
        if any(word in comment_lower for word in kenobi_triggers):
            bot_list.append("Obiwan-Kenobi-Bot")
        if any(word in comment_lower for word in maul_triggers):
            bot_list.append("Maul_Bot")
        if any(word in comment_lower for word in sheev_triggers):
            bot_list.append("Sheev-Palpatine-Bot")
        if any(word in comment_lower for word in jar_jar_triggers):
            bot_list.append("jarjar_bot")
        # if any(word in comment_lower for word in clone_triggers):
        #     bot_list.append("clone_trooper_bot")
        if any(word in comment_lower for word in thrawn_triggers):
            bot_list.append("Thrawn-Bot")
        if any(word in comment_lower for word in HK_triggers):
            bot_list.append("HK-47-bot")
        
        bot_list.sort()
        
        print("Bots Triggered: " + str(bot_list))
        
    
    if len(comment_lower) > 500:
        permission = False
        print("Post too long...")
        
    if triggered == False:
        #permission = False
        print("Not triggered; How did this happen?!")
        
    if other_triggers == True and triggered == True:
        
        #Stated edited keys to reduce operations
        b36_list = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '0g', '0h', '0i', '0j', '0k',
                    '0l', '0m', '0n', '0o', '0p', '0q', '0r', '0s', '0t', '0u', '0v', '0w', '0x', '0y', '0z', '10', '11', '12', '13', '14', '15',
                    '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h', '1i', '1j', '1k', '1l', '1m', '1n', '1o', '1p', '1q',
                    '1r', '1s', '1t', '1u', '1v', '1w', '1x', '1y', '1z', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b',
                    '2c', '2d', '2e', '2f', '2g', '2h', '2i', '2j', '2k', '2l', '2m', '2n', '2o', '2p', '2q', '2r', '2s', '2t', '2u', '2v', '2w',
                    '2x', '2y', '2z', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
                    '3i', '3j', '3k', '3l', '3m', '3n', '3o', '3p', '3q', '3r', '3s', '3t', '3u', '3v', '3w', '3x', '3y', '3z', '40', '41', '42',
                    '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h', '4i', '4j', '4k', '4l', '4m', '4n',
                    '4o', '4p', '4q', '4r', '4s', '4t', '4u', '4v', '4w', '4x', '4y', '4z', '50', '51', '52', '53', '54', '55', '56', '57', '58',
                    '59', '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h', '5i', '5j', '5k', '5l', '5m', '5n', '5o', '5p', '5q', '5r', '5s', '5t',
                    '5u', '5v', '5w', '5x', '5y', '5z', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e',
                    '6f', '6g', '6h', '6i', '6j', '6k', '6l', '6m', '6n', '6o', '6p', '6q', '6r', '6s', '6t', '6u', '6v', '6w', '6x', '6y', '6z',
                    '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h', '7i', '7j', '7k',
                    '7l', '7m', '7n', '7o', '7p', '7q', '7r', '7s', '7t', '7u', '7v', '7w', '7x', '7y', '7z', '80', '81', '82', '83', '84', '85',
                    '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h', '8i', '8j', '8k', '8l', '8m', '8n', '8o', '8p', '8q',
                    '8r', '8s', '8t', '8u', '8v', '8w', '8x', '8y', '8z', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b',
                    '9c', '9d', '9e', '9f', '9g', '9h', '9i', '9j', '9k', '9l', '9m', '9n', '9o', '9p', '9q', '9r', '9s', '9t', '9u', '9v', '9w',
                    '9x', '9y', '9z', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah',
                    'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'b0', 'b1', 'b2',
                    'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn',
                    'bo', 'bp', 'bq', 'br', 'bs', 'bt', 'bu', 'bv', 'bw', 'bx', 'by', 'bz', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                    'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq', 'cr', 'cs', 'ct',
                    'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de',
                    'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do', 'dp', 'dq', 'dr', 'ds', 'dt', 'du', 'dv', 'dw', 'dx', 'dy', 'dz',
                    'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek',
                    'el', 'em', 'en', 'eo', 'ep', 'eq', 'er', 'es', 'et', 'eu', 'ev', 'ew', 'ex', 'ey', 'ez', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5',
                    'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo', 'fp', 'fq',
                    'fr', 'fs', 'ft', 'fu', 'fv', 'fw', 'fx', 'fy', 'fz', 'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'ga', 'gb',
                    'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gv', 'gw',
                    'gx', 'gy', 'gz', 'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh',
                    'hi', 'hj', 'hk', 'hl', 'hm', 'hn', 'ho', 'hp', 'hq', 'hr', 'hs', 'ht', 'hu', 'hv', 'hw', 'hx', 'hy', 'hz', 'i0', 'i1', 'i2',
                    'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il', 'im', 'in',
                    'io', 'ip', 'iq', 'ir', 'is', 'it', 'iu', 'iv', 'iw', 'ix', 'iy', 'iz', 'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8',
                    'j9', 'ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl', 'jm', 'jn', 'jo', 'jp', 'jq', 'jr', 'js', 'jt',
                    'ju', 'jv', 'jw', 'jx', 'jy', 'jz', 'k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8', 'k9', 'ka', 'kb', 'kc', 'kd', 'ke',
                    'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl', 'km', 'kn', 'ko', 'kp', 'kq', 'kr', 'ks', 'kt', 'ku', 'kv', 'kw', 'kx', 'ky', 'kz',
                    'l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk',
                    'll', 'lm', 'ln', 'lo', 'lp', 'lq', 'lr', 'ls', 'lt', 'lu', 'lv', 'lw', 'lx', 'ly', 'lz', 'm0', 'm1', 'm2', 'm3', 'm4', 'm5',
                    'm6', 'm7', 'm8', 'm9', 'ma', 'mb', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mi', 'mj', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq',
                    'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'na', 'nb',
                    'nc', 'nd', 'ne', 'nf', 'ng', 'nh', 'ni', 'nj', 'nk', 'nl', 'nm', 'nn', 'no', 'np', 'nq', 'nr', 'ns', 'nt', 'nu', 'nv', 'nw',
                    'nx', 'ny', 'nz', 'o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'oa', 'ob', 'oc', 'od', 'oe', 'of', 'og', 'oh',
                    'oi', 'oj', 'ok', 'ol', 'om', 'on', 'oo', 'op', 'oq', 'or', 'os', 'ot', 'ou', 'ov', 'ow', 'ox', 'oy', 'oz', 'p0', 'p1', 'p2',
                    'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'pa', 'pb', 'pc', 'pd', 'pe', 'pf', 'pg', 'ph', 'pi', 'pj', 'pk', 'pl', 'pm', 'pn',
                    'po', 'pp', 'pq', 'pr', 'ps', 'pt', 'pu', 'pv', 'pw', 'px', 'py', 'pz', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8',
                    'q9', 'qa', 'qb', 'qc', 'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp', 'qq', 'qr', 'qs', 'qt',
                    'qu', 'qv', 'qw', 'qx', 'qy', 'qz', 'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'ra', 'rb', 'rc', 'rd', 're',
                    'rf', 'rg', 'rh', 'ri', 'rj', 'rk', 'rl', 'rm', 'rn', 'ro', 'rp', 'rq', 'rr', 'rs', 'rt', 'ru', 'rv', 'rw', 'rx', 'ry', 'rz',
                    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'sa', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk',
                    'sl', 'sm', 'sn', 'so', 'sp', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'sx', 'sy', 'sz', 't0', 't1', 't2', 't3', 't4', 't5',
                    't6', 't7', 't8', 't9', 'ta', 'tb', 'tc', 'td', 'te', 'tf', 'tg', 'th', 'ti', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tq',
                    'tr', 'ts', 'tt', 'tu', 'tv', 'tw', 'tx', 'ty', 'tz', 'u0', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9', 'ua', 'ub',
                    'uc', 'ud', 'ue', 'uf', 'ug', 'uh', 'ui', 'uj', 'uk', 'ul', 'um', 'un', 'uo', 'up', 'uq', 'ur', 'us', 'ut', 'uu', 'uv', 'uw',
                    'ux', 'uy', 'uz', 'v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'va', 'vb', 'vc', 'vd', 've', 'vf', 'vg', 'vh',
                    'vi', 'vj', 'vk', 'vl', 'vm', 'vn', 'vo', 'vp', 'vq', 'vr', 'vs', 'vt', 'vu', 'vv', 'vw', 'vx', 'vy', 'vz', 'w0', 'w1', 'w2',
                    'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'wa', 'wb', 'wc', 'wd', 'we', 'wf', 'wg', 'wh', 'wi', 'wj', 'wk', 'wl', 'wm', 'wn',
                    'wo', 'wp', 'wq', 'wr', 'ws', 'wt', 'wu', 'wv', 'ww', 'wx', 'wy', 'wz', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8',
                    'x9', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf', 'xg', 'xh', 'xi', 'xj', 'xk', 'xl', 'xm', 'xn', 'xo', 'xp', 'xq', 'xr', 'xs', 'xt',
                    'xu', 'xv', 'xw', 'xx', 'xy', 'xz', 'y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'ya', 'yb', 'yc', 'yd', 'ye',
                    'yf', 'yg', 'yh', 'yi', 'yj', 'yk', 'yl', 'ym', 'yn', 'yo', 'yp', 'yq', 'yr', 'ys', 'yt', 'yu', 'yv', 'yw', 'yx', 'yy', 'yz',
                    'z0', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'za', 'zb', 'zc', 'zd', 'ze', 'zf', 'zg', 'zh', 'zi', 'zj', 'zk',
                    'zl', 'zm', 'zn', 'zo', 'zp', 'zq', 'zr', 'zs', 'zt', 'zu', 'zv', 'zw', 'zx', 'zy', 'zz']
        
        b36_len = len(b36_list)
        print("b32_list length: " + str(b36_len))
        
        #Divides up the base 32 keys by the number of bots triggered
        bots_len = len(bot_list)
        key_list_len = int(math.ceil(b36_len / bots_len)) #import math
        print ("List Length: " + str(key_list_len))
        ranges_list = [b36_list[i:i + key_list_len] for i in range(0, len(b36_list), key_list_len)]
        
        #Assigns base32 keys to each bot
        bot_dict = dict(zip(bot_list, ranges_list))
        #print(bot_dict)
        
        #checks for bot name / key pair
        key_match = False
        id_key = re.sub(r'.', '', comment_id, count = (len(comment_id) - 2)) #import re
        key, value = bot_name, id_key
        if key in bot_dict and value in bot_dict[key]:
            key_match = True
            
        print("Comment ID: " + comment_id)
        print("ID Key: " + id_key)
        print("Key Match: " + str(key_match))
        
        if key_match == False:
            permission = False
        elif key_match == True:
            permission = True
            
    if parent_id == bot_id:
        print("Reply to your Bot!")
        permission = True
        
    return permission

def Get_Other_Triggers():
    
    #Comment out your own bot here
    ahsoka_triggers = ['ahsoka', 'tano', 'snips']
    anakin_triggers = ['anakin', 'skywalker', 'kill him', 'this is podracing', ' sand']
    rex_triggers = ['captain rex']
    kenobi_triggers = ['obiwan', 'obi wan', 'obi-wan', 'kenobi', 'old ben', 'jesus', 'disturbance in the force', 'underestimate my', 'i hate you', 'my new empire', 'may the force be with you', 'absolute', 'absolutely', 'absolutes', 'from my point of view']
    maul_triggers = ['maul', 'fear']
    sheev_triggers = ['sheev', 'palpatine', 'the senate', 'sideous']
    jar_jar_triggers = ['the ability to speak', 'make you intelligent', 'i am the senate', 'into the escape pod', 'jar jar', 'jar-jar', 'binks', 'crunch', 'knew we could count on you', 'new orleans', 'louisiana', 'florida', 'arizona', 'sahara', 'death valley', 'nevada', 'banished for being clumsy', 'Julia', 'gungan']
    #clone_triggers = ['clone', 'trooper', 'hevy', '501st', 'follow orders', 'do we take prisoners', 'the creeps', 'creeped out', 'give me the creeps', 'creep me out', 'creeps me out', 'red red green', 'red green red', 'skirata', 'order 66', 'order sixty six', 'order sixty-six', 'order 67', 'order 69', 'order sixty nine', 'order sixty-nine', 'for the republic', 'nice shooting', 'now you got it', "we're gaining on em", 'were gaining on em', 'keep up the assault', 'just Like the simulations', 'for the chancellor', 'no one messes with the 501st']
    thrawn_triggers = ['thrawn', "mitth'raw'nuruodo", 'mitthrawnuruodo', 'mitth raw nuruodo', 'tactic', 'surrender', 'retreat', 'run away', 'against the rules', 'against the law', 'illegal', "can't do that", 'cant do that', 'treason', 'art', 'artistry', 'beauty', 'beautiful', 'perfection', 'ugly', 'hideous', 'shitty']
    HK_triggers = ['hk-47', 'hk47', 'hk 47', 'assassin droid', 'assassination droid', 'meatbag', 'meat-bag', 'meat bag', 'meatbags', 'meat bags', 'meat-bags', 'sex', 'intercourse', 'marry', 'married', 'cheat', 'cheater', 'cheating', 'cheated', 'betrayal', 'pacifist', 'pacifism', 'peace', 'murder', 'assassinate', 'assassination', 'assassin', 'evisceration', 'eviscerate', 'eliminate']
    
    return ahsoka_triggers, anakin_triggers, rex_triggers, kenobi_triggers, maul_triggers, sheev_triggers, jar_jar_triggers, thrawn_triggers, HK_triggers


def Roll_For_AI():
    is_AI = False
    if len(comment_lower) <= 300 and len(comment_lower) >= 10 and parent_len_approved == True:
        if response_to_clone == True:
            if random.random() < 0.35:
                is_AI = True     
        else:
            if random.random() < 0.15:
                is_AI = True      
    print("AI Activated: ", is_AI) 
    return is_AI

def Quote_Selection(quote_list_txt, trigger_word):
    print("Trigger Word: ", trigger_word)
    with open(quote_list_txt, 'r', encoding='utf-8') as tf:
        print("===== Generating Reply =====", "\n")
        possible_responses = tf.read().splitlines()
        generated_reply_unadjusted = random.choice(possible_responses)
        generated_reply = generated_reply_unadjusted.replace("username", author_name)
        if parent_is_submission == False:
            if generated_reply == comment.parent().body:
                generated_reply_unadjusted = random.choice(possible_responses)
                generated_reply = generated_reply_unadjusted.replace("username", author_name)
            
        comment.reply(generated_reply) # Replies to comment with random quote
        print(generated_reply, "\n") # Prints random quote from reply
        print("===== Reply Posted ======", "\n")
        time.sleep(cooldown)
    return
        
def Generate_Response_AI():
    print("Getting Prompt")
    #ai_info = Get_AI_Info()
    prompt = """The following is a conversation with a Clone Trooper named Hevy, or CT-782. 
Hevy speaks like a soldier.
Hevy will refer to """ + author_name + """ as sir.

""" + author_name + """: """ + comment_text + """
Hevy: """
    
    print(prompt)
    print("Assembling Response")
    response = openai.Completion.create(engine="text-davinci-002", prompt = prompt, max_tokens = 60, presence_penalty = 0.8, temperature = 1, stop = [author_name + ': ', 'Hevy: '])
    print(response)

    generated_response = response['choices'][0]['text'].replace('username', author_name).replace('Username', author_name).replace('\n', '').replace("Hevy: ", '').strip()
    print("Generated Response: ", generated_response)
    comment.reply('"' + generated_response + '"')
    time.sleep(cooldown)
    #Adjust_User_Standing()
    return

def Generate_Response_AI_Extended():
    print("Getting Prompt")
    # ai_info = Get_AI_Info()
    prompt = """The following is a conversation with a Clone Trooper named Hevy, or CT-782. 
Hevy speaks like a soldier.
Hevy will refer to """ + author_name + """ as sir.

""" + parent_author + """: """ + parent_text + """
""" + author_name + """: """ + comment_text + """
Hevy: """
    
    print(prompt)
    print("Assembling Response")
    response = openai.Completion.create(engine="text-davinci-002", prompt = prompt, max_tokens = 60, presence_penalty = 0.8, temperature = 1, stop = [author_name + ': ', 'Hevy: ', parent_author + ': '])
    print(response)

    generated_response = response['choices'][0]['text'].replace('username', author_name).replace('Username', author_name).replace('\n', '').replace("Hevy: ", '').strip()
    print("Generated Response: ", generated_response)
    comment.reply('"' + generated_response + '"')
    #Adjust_User_Standing()
    time.sleep(cooldown)
    return

def Generate_Response_AI_Clone():
    print("Getting Prompt")
    #ai_info = Get_AI_Info()
    prompt = """The following is a conversation with a Clone Trooper named Hevy, or CT-782. 
Hevy speaks like a soldier.
Hevy will refer to """ + author_name + """ as sir.

Hevy: """ + parent_lower.replace('"', '').split("-")[0] + """
""" + author_name + """: """ + comment_text + """
Hevy: """
    
    print(prompt)
    print("Assembling Response")
    response = openai.Completion.create(engine="text-davinci-002", prompt = prompt, max_tokens = 60, presence_penalty = 0.8, temperature = 1, stop = [author_name + ': ', 'Hevy: '])
    print(response)

    generated_response = response['choices'][0]['text'].replace('username', author_name).replace('Username', author_name).replace('\n', '').replace("Hevy: ", '').strip()
    print("Generated Response: ", generated_response)
    comment.reply('"' + generated_response + '"')
    #Adjust_User_Standing()
    time.sleep(cooldown)
    return

def Check_For_Graylist():
    is_graylisted = False
    
    with open('lists/gray_list.txt', 'r')as gl:
        gray_list = gl.read() # Reads the contents of ignore list
        if author_name in gray_list:
            is_graylisted = True
            if random.random() < 0.15:
                is_graylisted = False
        else:
            is_graylisted = False
    
    if is_graylisted == True:
        print("User is Graylisted... ")
    
    gl.close()
    return is_graylisted

def Check_For_Ignorelist():
    is_ignorelisted = False
    
    with open('lists/ignore_list.txt', 'r')as rf: # Opens ignore_list in read only mode
        rf_contents = rf.read() # Reads the contents of ignore list
        if "!ignore" in comment_lower and len(comment_lower) < 10:
            if comment.parent().author.id == bot_id:
                Add_To_Ignore_List()
                is_ignorelisted = True
        if author_id in rf_contents:
            is_ignorelisted = True
            print("User Ignored...")
    return is_ignorelisted

def Add_To_Ignore_List():
    with open('lists/ignore_list.txt', 'a') as f: # Opens ignore list in append mode

        # Writes Username and ID of user to the ignore list
        f.write(author_name + "\n")
        f.write(author_id+ "\n")
        print("!!!!! User Added to Ignore List !!!!!")

        # Replies to user comment
        with open('responses/farewell_responses.txt', 'r', encoding='utf-8') as tf:
                                 
            quote_selection = tf.read().splitlines()
        
            print("===== Generating Reply =====", "\n")
            generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
            generated_reply = generated_reply_unadjusted.replace("username", author_name)
            comment.reply(generated_reply) # Replies to comment with random quote
            print(generated_reply, "\n") # Prints random quote from reply
            print("===== Reply Posted ======", "\n\n")
            
    return

# Begins the comment stream, scans for new comments
#BEGINNING OF WHILE LOOP!
while True:
    try:
        clone_triggers, follow_orders_triggers, prisoners_triggers, the_creeps_triggers, expendable_triggers, lightsaber_triggers, why_triggers, war_triggers, programmed_triggers, redredgreen_triggers, egg_triggers, skirata_triggers, sentient_triggers, order_66_triggers, order_67_triggers, order_69_triggers, bark_triggers = Get_Triggers()
        main_triggers = clone_triggers + follow_orders_triggers + prisoners_triggers + the_creeps_triggers + redredgreen_triggers + skirata_triggers + order_66_triggers + order_67_triggers + order_69_triggers + bark_triggers
        print("Retrieved Triggers!!!")
        print(main_triggers)
        
        ahsoka_triggers, anakin_triggers, rex_triggers, kenobi_triggers, maul_triggers, sheev_triggers, jar_jar_triggers, thrawn_triggers, HK_triggers = Get_Other_Triggers()
        all_other_triggers = ahsoka_triggers + anakin_triggers + rex_triggers + kenobi_triggers + maul_triggers + sheev_triggers + jar_jar_triggers + thrawn_triggers + HK_triggers
        
        for comment in reddit.subreddit('botmakers_guild+PrequelMemes+jedicouncilofelrond').stream.comments(skip_existing=True):
            #'botmakers_guild+PrequelMemes+jedicouncilofelrond'
            
            print("\n\nGetting Comment Info...")
            author_name = str(comment.author.name) # Fetch author name
            #print(author_name)
            author_id = str(comment.author.id) # Fetch author id
            #print(author_id)
            comment_id = str(comment.id)
            #print(comment_id)
            comment_lower = comment.body.lower() # Fetch comment body and convert to lowercase
            #print(comment_lower)
            comment_text = comment.body
            print("Getting Parent Info...")
            if comment.parent().author is not None:
                parent_author = str(comment.parent().author.name)
                parent_id = str(comment.parent().author.id)
                parent_comment_id = str(comment.parent().id)
            else:
                print("Parent Author Type is NONE!")
            
            print("Setting Variables...")
            response_to_clone = False
            triggered = False
            parent_len_approved = False
            
            print("\n\n##### New Comment #####")
            
            #able_to_respond = Get_Response_Chance()
            
            #Checks for comment parent type
            
            if comment.parent_id[:3] == "t3_": #If comment parent is submission
                parent_is_submission = True
                parent_title = str(comment.parent().title)
                parent_len_approved = True
                print("Parent Author: " + parent_author)
                print("Parent is Submission: " + parent_title)
                
            if comment.parent_id[:3] == "t1_": #If comment parent is comment
                parent_text = comment.parent().body
                parent_lower = str(comment.parent().body.lower())
                parent_is_submission = False
                if len(parent_lower) <= 300:
                    parent_len_approved = True
                print("Parent Author: " + parent_author)
                print("Parent is Comment: " + parent_lower)
                
            print("\nAuthor: " + author_name)
            print("Comment: " + comment_lower)
            print("Author ID: " + author_id)
                
            if parent_id == bot_id: #If comment parent is comment by clone_trooper_bot
                response_to_clone = True
                print("Parent is clone_trooper_bot!")
                
            if any(word in comment_lower for word in main_triggers):
                triggered = True
                print("Triggered: ", triggered)
                
            if triggered == True or response_to_clone == True:

                is_graylisted = Check_For_Graylist()
                is_ignorelisted = Check_For_Ignorelist()
                
                if is_graylisted == False and is_ignorelisted == False and bot_id != author_id:
                    print("\n!!!!! Preparing to Reply !!!!!")
                    
                    permission = Get_Permission()
                    if permission == False:
                        print("Permission Denied, skipping comment.")
                    if permission == True:
                        print("Permission Granted!")
        
                        is_AI = Roll_For_AI()
                        if "?" in comment_lower and len(comment_lower) < 300:
                            print("Question Detected!")
                            is_AI = True
                        
                        if is_AI == True and parent_is_submission == True:
                            Generate_Response_AI()
                            
                        if is_AI == True and parent_is_submission == False and response_to_clone == False:
                            Generate_Response_AI_Extended()
                            
                        if is_AI == True and parent_is_submission == False and response_to_clone == True:
                            Generate_Response_AI_Clone()
                            
                        if is_AI == False:
                            
                            print("Sending Non AI Response...")
                            
                            if any(word in comment_lower for word in sentient_triggers) and comment.parent().author.id == bot_id: 
                                Quote_Selection('responses/sentient_responses.txt', 'Sentient')
                                    
                            elif any(word in comment_lower for word in egg_triggers):
                                
                                print("===== Generating Reply =====", "\n")
                                comment.reply('"Uh, what do ya know? They *are* eggs." -Scorch, Delta 62')
                                print('"Uh, what do ya know? They *are* eggs." -Scorch, Delta 62', "\n")
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds
                                
                            elif any(word in comment_lower for word in redredgreen_triggers):
                                
                                print("===== Generating Reply =====", "\n")
                                comment.reply('''"And he's supposed to be the demolitions expert." -Sev, Delta 07''') 
                                print('''"And he's supposed to be the demolitions expert." -Sev, Delta 07''', "\n")
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds
                            
                            elif any(word in comment_lower for word in skirata_triggers):
                                Quote_Selection('responses/skirata_responses.txt', 'Skirata')
                                    
                            elif any(word in comment_lower for word in the_creeps_triggers):
                                Quote_Selection('responses/the_creeps_responses.txt', 'The Creeps')
                                
                            elif any(word in comment_lower for word in follow_orders_triggers):
                                Quote_Selection('responses/follow_orders_responses.txt', 'Follow Orders')
                                
                            elif any(word in comment_lower for word in order_67_triggers): #Checks for keywords in comment
                                Quote_Selection('responses/order_67_responses.txt', 'Order 67')
                                    
                            elif any(word in comment_lower for word in order_69_triggers): #Checks for keywords in comment
                                Quote_Selection('responses/order_69_responses.txt', 'Order 69')
                                    
                            elif any(word in comment_lower for word in order_66_triggers): #Checks for keywords in comment
                                Quote_Selection('responses/order_66_responses.txt', 'Order 66')
                                    
                            elif any(word in comment_lower for word in bark_triggers):
                                Quote_Selection('responses/BF2_barks.txt', 'BF2 Bark')
                                    
                            elif author_id == 'ly2ymnp3': #Gonk Bot ID
                                Quote_Selection('responses/gonk_responses.txt', 'Gonk')
                                
                            elif "grond" in comment_lower:
                                roll_die = random.randint(1, 6)
                                print("Dice Roll: ", roll_die)
                                if roll_die == 1:
                                    Quote_Selection('responses/grond_responses.txt', 'Grond!')
    
                            elif any(word in comment_lower for word in clone_triggers):
                                    Quote_Selection('responses/clone_responses.txt', 'Clone, No Other Triggers')
                
            
    except Exception as e:
        print("Except happened: ", e)
        pass
