# housekeeping script;
# prepares the environment for the next day
import re, os, subprocess

### START HELPER FNS ###

# format handler
def pad(val):
    if val < 10:
        val = '0{}'.format(val)
    return str(val)

#exception handlers
def tidy_pass(args):
    code, cmd = args[0], ' '.join(args[1])
    print('Err_{}_{}: execution unsuccessful -- {}'.format(code, 'recoverable', cmd))
    pass

def tidy_exit(args):
    code, cmd = args[0], ' '.join(args[1])
    print('Err_{}_{}: execution unsuccessful -- {}'.format(code, 'catastrophic', cmd))
    exit(1)

### END HELPER FNS ###

# identify day values in current directory
dirs = next(os.walk('.'))[1]
dirs = ' '.join(dirs)
days = re.findall('day_[0-9]{2}', dirs)

# identify previous and next day numerical value
prev_day, next_day = 0, None
for day in days:
    if int(day[-2:]) > prev_day:
        prev_day = int(day[-2:])
next_day = pad(prev_day + 1)
prev_day = pad(prev_day)

# git cleanup and next day preparations
try:
    subprocess.run(['git', 'checkout', 'main'], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['git', 'pull'], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['git', 'branch', '-d', 'day_{}'.format(prev_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_pass(err.args)
try:
    subprocess.run(['git', 'remote', 'update', 'origin', '--prune'], check=True)
except subprocess.CalledProcessError as err:
    tidy_pass(err.args)
try:
    subprocess.run(['git', 'branch', 'day_{}'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['git', 'checkout', 'day_{}'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)

# next day preparations
try:
    subprocess.run(['mkdir', 'day_{}'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['cp', 'template.py', 'day_{}/part_a.py'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_pass(err.args)
try:
    subprocess.run(['cp', 'template.py', 'day_{}/part_b.py'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_pass(err.args)
try:
    subprocess.run(['touch', 'input_files/aoc_{}.txt'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_pass(err.args)
try:
    subprocess.run(['git', 'add', 'day_{}/part_*'.format(next_day), 'input_files/aoc_{}.txt'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['git', 'commit', 'day_{}/part_*'.format(next_day), 'input_files/aoc_{}.txt'.format(next_day), '-m', '"Feat: adds initial day {} files"'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)
try:
    subprocess.run(['git', 'push', '--set-upstream', 'origin', 'day_{}'.format(next_day)], check=True)
except subprocess.CalledProcessError as err:
    tidy_exit(err.args)

print('SUCCESS')