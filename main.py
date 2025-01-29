import random as r, string as s, keyboard as k, threading as t, json as j, os as o, ctypes as c, sys as y
p2 = 'config.json'
p3 = {
    'e': True,
    'a': None
}
def p4():
    return ''.join(r.choices(s.ascii_letters, k=8))
def p5():
    if o.path.exists(p2):
        try:
            with open(p2, 'r') as f:
                return {**p3, **j.load(f)}
        except (FileNotFoundError, j.JSONDecodeError):
            pass
    return p3
def p6(p7):
    with open(p2, 'w') as f:
        j.dump(p7, f)
def p8():
    def p9(e):
        global a1
        a1 = e.keysym
        p3['a'] = a1
        p6(p3)
        p10()
    import tkinter as t
    p11 = t.Tk()
    p11.title("Initial Setup")
    p12 = t.Label(p11, text="Press any key to activate Snap Tap")
    p12.pack(padx=20, pady=20)

    p11.bind("<KeyPress>", p9)
    p11.mainloop()
def p13():
    global b1
    b1 = not b1
    if not b1:
        k.release('a')
        k.release('d')
def p14():
    if b1:
        if c1['a'] and c1['d']:
            if d1 == 'a':
                k.press('a')
                k.release('d')
            elif d1 == 'd':
                k.press('d')
                k.release('a')
        elif c1['a']:
            k.press('a')
            k.release('d')
        elif c1['d']:
            k.press('d')
            k.release('a')
        else:
            k.release('a')
            k.release('d')
    else:
        k.release('a')
        k.release('d')
def p15(e1, f1):
    with g1:
        c1[e1] = f1
        global d1
        d1 = e1 if f1 else None
    p14()
def p10():
    global b1, c1, d1, g1
    b1 = p3['e']
    c1 = {'a': False, 'd': False}
    d1 = None
    g1 = t.Lock()
    k.on_press_key('a', lambda e: p15('a', True))
    k.on_release_key('a', lambda e: p15('a', False))
    k.on_press_key('d', lambda e: p15('d', True))
    k.on_release_key('d', lambda e: p15('d', False))
    if a1:
        k.add_hotkey(a1, p13)
    k.wait('F12')
def p16():
    if y.platform == 'win32':
        c.windll.user32.ShowWindow(c.windll.kernel32.GetConsoleWindow(), 0)
p3 = p5()
a1 = p3.get('a')
if a1:
    p16()
    p10()
else:
    p8()
