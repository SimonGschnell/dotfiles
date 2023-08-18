#os/fs
[[how to make a bootable USB-stick on linux]]

- [ ] **download** the iso file of your preferred linux distribution
- [ ] **plug into** your pc a usb stick with at least 32gb
- [ ] **Look up** the name of the usb-stick with the `lsblk` or `sudo fdisk -l` command. Most of the time, it will have the name      /dev/sda{1-5} or /dev/sdb. (I will use ***$usb_path*** for further references)
- [ ] **Unmount** the usb-stick, in order to format it. The unmount command will be:         `umount $usb_path*` (the \* symbol includes all)
- [ ] **Format** the usb-stick with the command: `sudo mkfs.ext4 /dev/sda` which will format it with the ext4 filesystem (ext4 is used for linux)
- [ ] **Install** the iso file to your usb-stick, we do that with the command: `sudo dd if=/path/to/your/iso of=$usb_path status='progress'`. Where if stands for **INPUT FILE** , of stands for **OUTPUT FILE** and we add **status='progress'** to see the progress of the installation, because normally there is no information when executing a dd command.

- NOW WE HAVE A BOOTABLE USB-STICK