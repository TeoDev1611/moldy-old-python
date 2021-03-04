package cmd

import (
	"fmt"
	//Comunnity package
	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

func tellInstall(module string) {
	color.Green("Installing the moldy module **" + module + "**")
	fmt.Println("Me has llamado")
}

// installCmd represents the install command
var installCmd = &cobra.Command{
	Use:   "install User/Repository",
	Short: "Install a package of Moldy",
	Long: `Install the package use.
	This clone the package in the current folder.`,
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) == 0 {
			color.Red("Error: Not found the module")
		} else {
			modulo := args[0]
			tellInstall(modulo)
		}

	},
}

func init() {
	rootCmd.AddCommand(installCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// installCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// installCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
