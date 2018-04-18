import subprocess

log = open('geth.log', 'a')

proc = subprocess.Popen([
    'geth',
    '--networkid', '16',
    '--port', '30303',
    '--maxpeers', '0',
    '--nodiscover',
    '--etherbase', '0x857b97371202791b18d415179c0fbfe16d28802d',
    '--mine',
], stderr=log)

print('process id = %d' % proc.pid)

# end of run.py
