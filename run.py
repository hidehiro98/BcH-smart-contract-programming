import subprocess

log = open('geth.log', 'a')

proc = subprocess.Popen([
    'geth',
    '--networkid', '16',
    '--port', '30303',
    '--maxpeers', '0',
    '--nodiscover',
    '--etherbase', '0x167576ad3ee015591cbd90ad3afa1fff6ac0d674',
    '--mine',
], stderr=log)

print('process id = %d' % proc.pid)

# end of run.py
