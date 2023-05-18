# Web stack debugging #3

This repository contains a script to fix a specific issue in WordPress by modifying the `wp-settings.php` file. The fix replaces occurrences of `phpp` with `php` in the mentioned file, resolving a problem that can cause a 500 error.

## Usage

1. Clone the repository
2. Navigate to the repository directory: cd 0x17-web_stack_debugging_3
3. Run the fix script: sudo puppet apply 0-strace_is_your_friend.pp This will execute the Puppet manifest `0-strace_is_your_friend.pp`, which applies the fix by using the `exec` resource to run the `sed` command.
4. Verify the fix: curl -sI 127.0.0.1

The output should now indicate a successful HTTP response without a 500 error.

## Requirements

- Puppet version 3.4 or higher
- Ubuntu 14.04 LTS
- LAMP stack with WordPress installed

## Note

Make sure to customize the `0-strace_is_your_friend.pp` file according to your specific environment and requirements before running the script.
