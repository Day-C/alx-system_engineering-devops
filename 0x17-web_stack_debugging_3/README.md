Using 'Strace' to debug an appahe server that returns a 500 error then automate it with puppet.
First i used strace to debug and find an error then used puppet for fixing the bug.
": the problem with the file was a type error made in the sttings.php file. i used a puppet manifest to correct the file
